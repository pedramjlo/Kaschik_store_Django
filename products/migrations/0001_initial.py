# Generated by Django 5.1.3 on 2024-12-03 19:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("price", models.IntegerField()),
                ("is_available", models.BooleanField(default=True)),
                ("on_discount", models.BooleanField(default=False)),
                ("available_sizes", models.JSONField(blank=True, default=list)),
                ("available_hues", models.JSONField(blank=True, default=list)),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="categories.category",
                    ),
                ),
            ],
        ),
    ]
