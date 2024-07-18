from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'ingredients', 'instructions','recipe_image']

# 1. class Meta
# In Django, class Meta is used to provide metadata about a model class. It allows you to specify options or configurations for the model without needing to define them directly in the model fields. Here’s how it works:

# Purpose: class Meta is used to give instructions or metadata to Django about how to handle a particular model class.

# Where to Use: You define class Meta inside a Django model class to provide additional information about the model’s behavior.

# Common Uses:

# Database Table Name: You can specify a custom database table name for the model.
# Ordering: You can define the default ordering of objects retrieved from the database.
# Unique Constraints: You can enforce uniqueness constraints on model fields.
# Permissions: You can specify permissions related to the model.
# Verbose Name: You can set a human-readable name for the model in Django's admin interface.
# Example:

# python
# Copy code
# from django.db import models

# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     class Meta:
#         verbose_name_plural = "My Models"
#         ordering = ['field1']
# In this example:

# verbose_name_plural specifies the plural name used in Django admin.
# ordering specifies that results should be ordered by field1 by default.
# 2. RecipeForm
# In Django, RecipeForm is a form class that you define to handle input data from users related to your Recipe model. It allows you to create, update, and validate data before saving it to the database. Here’s how it works:

# Purpose: RecipeForm is used to define how data related to a Recipe model should be presented in a web form.

# Where to Use: You define RecipeForm in a Django forms module (forms.py) inside your app directory.

# Common Features:

# Fields: You define form fields that correspond to model fields.
# Validation: You can add custom validation logic to ensure data integrity.
# Save Method: You can override the save() method to customize how data is saved to the database.
# Widgets: You can specify form widgets (e.g., text input, select dropdown) for each field.
# Integration: RecipeForm integrates seamlessly with Django views and templates to handle form rendering, submission, and validation.
# Example:

# python
# Copy code
# from django import forms
# from .models import Recipe

# class RecipeForm(forms.ModelForm):
#     class Meta:
#         model = Recipe
#         fields = ['recipe_name', 'recipe_description', 'recipe_image']
# In this example:

# RecipeForm is defined using forms.ModelForm, which automatically creates form fields based on the Recipe model fields.
# Meta class specifies the model attribute as Recipe and the fields attribute as a list of fields to include in the form (recipe_name, recipe_description, recipe_image).
# Summary
# class Meta provides metadata about a Django model class, influencing its behavior without altering the fields directly.
# RecipeForm is a Django form class that defines how data related to a Recipe model is presented and validated in web forms.
# Together, class Meta and RecipeForm streamline the process of interacting with data in Django applications, providing a clear structure for defining models and handling user input effectively.






