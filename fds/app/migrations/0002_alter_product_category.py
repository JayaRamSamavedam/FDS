# Generated by Django 4.1.2 on 2022-12-03 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('MT', 'MEN-TOPWEAR'), ('MB', 'MEN-BOTTOMWEAR'), ('WI', 'WOMEN-INDIAN'), ('WW', 'WOMEN-WESTERN')], max_length=2),
        ),
    ]