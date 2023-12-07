from rest_framework import serializers
from .models import Customer, Product, Order, OrderItem
from django.utils import timezone
from rest_framework.validators import UniqueValidator
from django.core.validators import MinValueValidator, MaxValueValidator





class CustomerSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Customer.objects.all())]
    )
    class Meta:
        model = Customer
        fields = ['name', 'contact_number', 'email']

    
    
class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField(
        max_length=255,
        validators=[UniqueValidator(queryset=Product.objects.all())]
    )

    weight = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        validators=[
            MinValueValidator(limit_value=0.01),
            MaxValueValidator(limit_value=25.00)
        ]
    )


    class Meta:
        model = Product
        fields = ['name', 'weight']




class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity']





class DateFormatField(serializers.DateField):
    def to_representation(self, value):
        return value.strftime('%d/%m/%Y') if value else None

    def to_internal_value(self, data):
        try:
            return timezone.datetime.strptime(data, '%d/%m/%Y').date()
        except (ValueError, TypeError):
            self.fail('invalid')





class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)
    order_date = DateFormatField()


    class Meta:
        model = Order
        fields = ['customer', 'order_date', 'address', 'order_item']



    def update(self, instance, validated_data):
        instance.customer = validated_data.get('customer', instance.customer)
        instance.order_date = validated_data.get('order_date', instance.order_date)
        instance.address = validated_data.get('address', instance.address)

        # Handle order_item update (assuming it's a related field)
        order_items_data = validated_data.get('order_item', [])
        for order_item_data in order_items_data:
            # Update existing order items or create new ones
            OrderItem.objects.update_or_create(order=instance, **order_item_data)

        instance.save()
        return instance


    def validate_cumulative_weight(self, data):
        # Order cumulative weight must be under 150kg
        cumulative_weight = sum(item['quantity'] * item['product'].weight for item in data['order_item'])
        print('****cumulative_weight****',cumulative_weight)
        if cumulative_weight > 150:
            raise serializers.ValidationError("Cumulative weight must be under 150kg.")
    

    def validate_order_date(self, value):
        # Order Date cannot be in the past
        print('value:', value)
        if value < timezone.now().date():
            raise serializers.ValidationError("Order date cannot be in the past.")
        return value


    
    def create(self, validated_data):
        print('***validated data***', validated_data)
        self.validate_cumulative_weight(validated_data)

        order_items_data = validated_data.pop('order_item')
        order = Order.objects.create(**validated_data)

        for order_item_data in order_items_data:
            OrderItem.objects.create(order=order, **order_item_data)

        return order

        
        