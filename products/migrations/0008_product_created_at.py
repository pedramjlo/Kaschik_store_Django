# Generated by Django 5.1.3 on 2024-12-04 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0007_alter_product_hue"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="created_at",
            field=models.DateField(auto_now=True),
        ),
    ]
