# Generated by Django 5.1.3 on 2024-12-07 11:13

import django.db.models.deletion
import iranian_cities.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "iranian_cities",
            "0009_rename_iranian_cit_code_1c3b38_idx_sage_city_code_8db749_idx_and_more",
        ),
        ("shopping_cart", "0005_alter_shoppingcartitem_quantity"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="shoppingcart",
            name="address",
        ),
        migrations.AddField(
            model_name="shoppingcart",
            name="customer_address",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="shoppingcart",
            name="customer_city",
            field=iranian_cities.fields.CityField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="iranian_cities.city",
            ),
        ),
        migrations.AddField(
            model_name="shoppingcart",
            name="customer_province",
            field=iranian_cities.fields.ProvinceField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="iranian_cities.province",
            ),
        ),
    ]
