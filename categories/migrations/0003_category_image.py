# Generated by Django 5.1.3 on 2024-12-04 07:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("avatars", "0001_initial"),
        ("categories", "0002_category_type"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="image",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="avatars.avatar",
            ),
        ),
    ]