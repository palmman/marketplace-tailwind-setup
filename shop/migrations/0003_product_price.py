# Generated by Django 4.0.2 on 2022-03-03 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_seller'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=7, null=True),
        ),
    ]
