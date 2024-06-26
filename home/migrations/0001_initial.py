# Generated by Django 4.2.10 on 2024-04-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("full_name", models.CharField(max_length=100)),
                ("company_name", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
            ],
        ),
    ]
