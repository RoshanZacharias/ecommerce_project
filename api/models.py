from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone
from django.core.exceptions import ValidationError




# Create your models here.
class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    

    
    def __str__(self):
        return self.name
    


class Product(models.Model):
    name = models.CharField(max_length=255)
    weight = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name
    


class Order(models.Model):
    order_number = models.CharField(max_length=20, unique=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    order_date = models.DateField()
    address= models.CharField(max_length=255)
    
    
    def save(self, *args, **kwargs):
        if not self.order_number:
            last_order = Order.objects.order_by('-id').first()
            if last_order:
                last_number = int(last_order.order_number[3:])
                self.order_number= f"ORD{str(last_number + 1).zfill(5)}"
            else:
                self.order_number = 'ORD00001'
        
        super(Order, self).save(*args, **kwargs)
    

    def __str__(self):
        return f"{self.order_number} - {self.customer.name}"
    



class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_item', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    


    def __str__(self):
        return f"{self.order.order_number} {self.product.name} - Quantity: {self.quantity}"
    