# Generated by Django 4.1.2 on 2022-12-03 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_product_colour_product_fabric_product_sizes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='feedback',
            field=models.CharField(default=' ', max_length=100),
        ),
    ]
