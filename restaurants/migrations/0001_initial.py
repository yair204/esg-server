# Generated by Django 5.0.6 on 2024-06-04 11:31

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Restaurant",
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
                ("name", models.CharField(max_length=255)),
                (
                    "coordinates",
                    django.contrib.gis.db.models.fields.PointField(
                        blank=True, null=True, srid=4326
                    ),
                ),
                ("phone", models.CharField(blank=True, max_length=20)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("italian", "Italian"),
                            ("mexican", "Mexican"),
                            ("pizza", "Pizza"),
                            ("fleshy", "Fleshy"),
                            ("dairy", "Dairy"),
                        ],
                        max_length=50,
                    ),
                ),
                ("open_hour", models.TimeField(blank=True, null=True)),
                ("close_hour", models.TimeField(blank=True, null=True)),
            ],
        ),
    ]