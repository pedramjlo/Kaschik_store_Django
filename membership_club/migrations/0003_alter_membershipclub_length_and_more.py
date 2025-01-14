# Generated by Django 5.1.3 on 2024-12-07 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("membership_club", "0002_membershipclub_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipclub",
            name="length",
            field=models.CharField(
                choices=[
                    ("onemonth", "OneMonth"),
                    ("threemonths", "ThreeMonths"),
                    ("oneyear", "OneYear"),
                ],
                max_length=15,
            ),
        ),
        migrations.AlterField(
            model_name="membershipclub",
            name="type",
            field=models.CharField(
                choices=[
                    ("onemonth", "OneMonth"),
                    ("threemonths", "ThreeMonths"),
                    ("oneyear", "OneYear"),
                ],
                max_length=11,
            ),
        ),
    ]
