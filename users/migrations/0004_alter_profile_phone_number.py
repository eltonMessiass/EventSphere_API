# Generated by Django 5.1 on 2024-08-23 08:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_profile_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.CharField(
                blank=True,
                max_length=9,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Invalid Phone number", regex="^8[2-7]\\d{7}$"
                    )
                ],
            ),
        ),
    ]
