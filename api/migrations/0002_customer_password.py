# Generated by Django 4.2.3 on 2023-12-06 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='password',
            field=models.CharField(default='default_password', max_length=20),
        ),
    ]
