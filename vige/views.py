from django.shortcuts import get_object_or_404, render,redirect
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import vercel_blob

from langchain_openai import ChatOpenAI
import os

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=OPENAI_API_KEY)


# Create your views here.s
@login_required(login_url='/login/')
def recipe_view(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False);
            file = request.FILES['recipe_image']
            upload_data= vercel_blob.put(file.field_name, file.read(), {})
            recipe_image_url = upload_data['url']
            recipe.recipe_image = recipe_image_url
            recipe.user = request.user 
            recipe.save()
            return redirect('recipe_view')
        else:
            print(form.errors)  
    else:
        form = RecipeForm()
    # recipes = Recipe.objects.all()
    recipes = Recipe.objects.filter(user=request.user)
    
    # Retrieve the generated recipe from the session
    generated_recipe = request.session.pop('generated_recipe', None)
    if generated_recipe:
        form = RecipeForm(initial={
            'title': generated_recipe['title'],
            'ingredients': generated_recipe['ingredients'],
            'instructions': generated_recipe['instructions']
        })

    return render(request, 'recipe.html', {'form': form, 'recipes': recipes})

@login_required(login_url='/login/')
def delete_recipe_view(request,id):
    # recipe=Recipe.objects.get(id=id)
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    if recipe.user == request.user:
        if str(recipe.recipe_image):
          print(recipe.recipe_image)
          vercel_blob.delete(str(recipe.recipe_image))
        recipe.delete()
        messages.success(request, "Recipe deleted successfully.")
    else:
        messages.error(request, "You do not have permission to delete this recipe.")
    return redirect('recipe_view')

@login_required(login_url='/login/')
def recipe_update_view(request, id):
    # recipe = get_object_or_404(Recipe, id=id)
    recipe = get_object_or_404(Recipe, id=id, user=request.user)
    old_recipe_image_url=recipe.recipe_image
    
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            if 'recipe_image' in request.FILES:
               recipe = form.save(commit=False)
               file = request.FILES['recipe_image']
               if str(old_recipe_image_url):
                  vercel_blob.delete(str(old_recipe_image_url))
               upload_data= vercel_blob.put(file.field_name, file.read(), {})
               recipe_image_url = upload_data['url']
               recipe.recipe_image = recipe_image_url
               form.save()
               messages.success(request, "Recipe updated successfully.")
            else:
                form.save() 
            return redirect('recipe_view')
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipe_update.html', {'form': form, 'recipe': recipe})

@login_required(login_url='/login/')       
def generate_recipe(request):
    if request.method == 'POST':
      cuisine_type = request.POST.get('cuisine_type')
      main_ingredient = request.POST.get('main_ingredient')
      dietary_preference = request.POST.get('dietary_preference')
      prompt = f"Generate a {cuisine_type} recipe using {main_ingredient} that is {dietary_preference}. Include a title and detailed instructions."
      response=llm.invoke(prompt)
      recipe_text = response.content

      # Splitting the response to extract the title and recipe
      parts = recipe_text.split('\n\n', 1)
      recipe_title = parts[0].replace('Title: ', '')
      recipe_details = parts[1].split('\n\nInstructions:', 1)
      recipe_ingredients = recipe_details[0].replace('Ingredients:\n', '')
      recipe_instructions = recipe_details[1] if len(recipe_details) > 1 else "No instructions provided."
      
      recipe = {
                'title': recipe_title,
                'ingredients': recipe_ingredients,
                'instructions': recipe_instructions,

      }
      request.session['generated_recipe'] = recipe
      return redirect("recipe_view")
  
    return render(request, 'generate_recipe.html')

@login_required(login_url='/login/')
def logout_page(request):
    logout(request)
    return redirect('login_page')
        
def register_page(request):
    if request.method == 'POST':
        userName = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        # Check if a user with the same username or email already exists
        if User.objects.filter(username=userName).exists():
            messages.error(request, "Account with this username already exists.")
            return redirect('register_page')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, "Account with this email already exists.")
            return redirect('register_page')
        
        # Create a new user
        user = User.objects.create(username=userName, email=email)
        user.set_password(password)
        user.save()
        
        messages.success(request, "Account created successfully.")
        return redirect('login_page')
    
    return render(request, 'register.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Check if the username exists
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Account with this username does not exist.")
            return redirect('login_page')
        
        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is None:
            messages.error(request, "Invalid username or password.")
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('recipe_view')
    
    return render(request, 'login.html')

