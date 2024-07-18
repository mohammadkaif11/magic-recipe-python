# Generated by Django 5.0.7 on 2024-07-15 06:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("vige", "0003_recipe_user"),
    ]

    operations = [
        migrations.RenameField(
            model_name="recipe",
            old_name="recipe_description",
            new_name="ingredients",
        ),
        migrations.RenameField(
            model_name="recipe",
            old_name="recipe_name",
            new_name="title",
        ),
        migrations.AddField(
            model_name="recipe",
            name="instructions",
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
