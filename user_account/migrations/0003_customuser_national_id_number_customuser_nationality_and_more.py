# Generated by Django 5.1.3 on 2024-12-03 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_account", "0002_customuser_phone_number"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="national_id_number",
            field=models.PositiveBigIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="customuser",
            name="nationality",
            field=models.CharField(
                blank=True,
                choices=[("iranian", "Iranian"), ("foreigner", "Foreigner")],
                max_length=9,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="customuser",
            name="passport_number",
            field=models.CharField(blank=True, max_length=9, null=True),
        ),
    ]