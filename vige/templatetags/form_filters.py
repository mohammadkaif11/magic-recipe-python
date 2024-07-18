from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(value, arg):
    return value.as_widget(attrs={'class': arg})


# The custom template filter add_class is designed to dynamically add a CSS class to form fields in Django templates. This can be useful for applying consistent styling to form elements using a CSS framework like Bootstrap.

# Here’s how the custom filter works:

# Filter Definition:

# The filter is defined in a Python file within the templatetags directory of your Django app.
# The filter function add_class takes two arguments: value (the form field) and arg (the CSS class to be added).
# Filter Functionality:

# The filter uses the as_widget method of the form field to modify its attributes.
# The attrs parameter of as_widget is used to add the specified CSS class.
# Detailed Steps to Implement and Use the Filter
# Create templatetags Directory and form_filters.py File:

# In your Django app directory (e.g., recipes), create a directory named templatetags.
# Inside templatetags, create an empty __init__.py file and a form_filters.py file.
# markdown
# Copy code
# recipes/
# ├── templatetags/
# │   ├── __init__.py
# │   └── form_filters.py
# Define the Custom Template Filter in form_filters.py:

# python
# Copy code
# from django import template

# register = template.Library()

# @register.filter(name='add_class')
# def add_class(value, arg):
#     return value.as_widget(attrs={'class': arg})
# template.Library() creates a new template library.
# @register.filter(name='add_class') registers the add_class function as a template filter named add_class.
# The add_class function takes value (a form field) and arg (the CSS class) as arguments and returns the form field with the added class using as_widget.
# Load the Custom Template Filter in Your Template:

# At the top of your template (e.g., recipe_update.html), load the custom template filter:

# html
# Copy code
# {% load form_filters %}
# Use the Custom Filter in Your Template:


# {% extends "base.html" %}

# {% block title %}
#     Update Recipe - My Site
# {% endblock %}

# {% block start %}
# <div class="container my-4">
#     <div class="card">
#         <div class="card-header">
#             <h4>Update Recipe</h4>
#         </div>
#         <div class="card-body">
#             <form method="post" enctype="multipart/form-data">
#                 {% csrf_token %}
#                 <div class="form-group">
#                     <label for="recipeName">Recipe Name</label>
#                     {{ form.recipe_name|add_class:"form-control" }}
#                 </div>
#                 <div class="form-group">
#                     <label for="recipeDescription">Recipe Description</label>
#                     {{ form.recipe_description|add_class:"form-control" }}
#                 </div>
#                 <div class="form-group">
#                     <label for="recipeImage">Upload Image</label>
#                     {{ form.recipe_image|add_class:"form-control-file" }}
#                 </div>
#                 <button type="submit" class="btn btn-primary">Update Recipe</button>
#             </form>
#             <a href="{% url 'recipe_view' %}" class="btn btn-secondary mt-2">Cancel</a>
#         </div>
#     </div>
# </div>
# {% endblock %}


