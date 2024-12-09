# Generated by Django 5.1.2 on 2024-12-09 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=4, default=0, max_digits=11),
        ),
    ]
