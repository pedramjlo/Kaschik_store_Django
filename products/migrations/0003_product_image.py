# Generated by Django 5.1.3 on 2024-12-04 09:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avatars", "0002_alter_avatar_image"),
        ("products", "0002_size_remove_product_available_hues_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="avatars.avatar",
            ),
        ),
    ]