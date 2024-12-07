# Generated by Django 5.1.3 on 2024-12-07 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("membership_club", "0003_alter_membershipclub_length_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipclub",
            name="type",
            field=models.CharField(
                choices=[
                    ("regular", "Regular"),
                    ("bronze", "Bronze"),
                    ("silver", "Silver"),
                    ("vip", "VIP"),
                ],
                max_length=11,
            ),
        ),
    ]
