# Generated by Django 5.1.3 on 2024-12-07 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("membership_club", "0008_alter_membershipclub_length_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="membershipclub",
            name="user",
        ),
    ]
