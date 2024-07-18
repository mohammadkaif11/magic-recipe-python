from django.db import models
#Adding Authentication
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    # user = models.ForeignKey(User,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    title = models.CharField(max_length=100,null=False)
    ingredients = models.TextField(null=False)
    instructions = models.TextField(null=False, default="Default Instructions")
    # recipe_image = models.ImageField(upload_to="uploads",null=False)
    recipe_image = models.ImageField(null=False)

    