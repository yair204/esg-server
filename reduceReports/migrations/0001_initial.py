# Generated by Django 5.0.6 on 2024-06-06 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ReduceReport",
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
                ("company_name", models.CharField(max_length=255)),
                ("date", models.DateField()),
                ("electricity", models.DecimalField(decimal_places=2, max_digits=10)),
                ("gas", models.DecimalField(decimal_places=2, max_digits=10)),
                ("water", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
    ]
