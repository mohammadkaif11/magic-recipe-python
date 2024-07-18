"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from home.views import *
from vige.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',home),
    path('recipe/',recipe_view,name='recipe_view'),
    path('generate-recipe/',generate_recipe,name='generate_recipe'),
    path('delete-recipe/<id>/',delete_recipe_view,name='delete_recipe'),
    path('update-recipe/<int:id>/',recipe_update_view, name='recipe_update_view'),
    path('login/',login_page,name='login_page'),
    path('register/',register_page,name='register_page'),
    path('logout/',logout_page,name='logout_page'),

    path("admin/", admin.site.urls),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

