from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required

# def home(request):
#     return HttpResponse("Hey I am a django server")

# return template  sending data to page by context

@login_required(login_url='/login')
def home(request):
    context = {
        'title': 'My Awesome Site',
        'items': ['Item 1', 'Item 2', 'Item 3']
    }
    return render(request,"index.html",context)
