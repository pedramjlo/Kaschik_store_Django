# Generated by Django 5.1.3 on 2024-12-04 07:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avatars", "0001_initial"),
        ("categories", "0003_category_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="image",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="avatars.avatar",
            ),
        ),
    ]
