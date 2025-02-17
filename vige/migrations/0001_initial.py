# Generated by Django 5.0.6 on 2024-07-10 05:06

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Ricepe",
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
                ("ricepe_name", models.CharField(max_length=100)),
                ("ricepe_description", models.TextField()),
                ("ricepe_image", models.ImageField(upload_to="uploads")),
            ],
        ),
    ]
