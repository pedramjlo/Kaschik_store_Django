# Generated by Django 5.1.3 on 2024-12-07 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("membership_club", "0005_alter_membershipclub_end_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membershipclub",
            name="price",
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
