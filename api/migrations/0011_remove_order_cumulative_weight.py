# Generated by Django 5.0 on 2023-12-07 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_alter_customer_name_alter_orderitem_order_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='cumulative_weight',
        ),
    ]
