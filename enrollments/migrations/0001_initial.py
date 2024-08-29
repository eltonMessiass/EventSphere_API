# Generated by Django 5.1 on 2024-08-29 05:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0002_rename_descriptiom_event_description"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Enrollment",
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
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("confirmed", "Confirmed"),
                            ("pending", "Pending"),
                            ("canceled", "Canceled"),
                        ],
                        default="PENDING",
                        max_length=10,
                    ),
                ),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="events.event"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Ticket",
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
                ("code", models.CharField(max_length=100, unique=True)),
                ("issue_date", models.DateTimeField(auto_now_add=True)),
                ("is_used", models.BooleanField(default=False)),
                (
                    "enrollment",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="assigned_ticket",
                        to="enrollments.enrollment",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="enrollment",
            name="ticket",
            field=models.OneToOneField(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="enrollment_ticket",
                to="enrollments.ticket",
            ),
        ),
    ]
