# vige/middleware.py

from django.http import HttpResponseRedirect
from django.urls import reverse

class AuthRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path == reverse('login_page'):
            return self.get_response(request)

        if not request.user.is_authenticated:
            # Redirect to your login page
            return HttpResponseRedirect(reverse('login_page'))
        
        response = self.get_response(request)
        return response

# UPDATE Settings.py 
# MIDDLEWARE = [
#     "django.middleware.security.SecurityMiddleware",
#     "django.contrib.sessions.middleware.SessionMiddleware",
#     "django.middleware.common.CommonMiddleware",
#     "django.middleware.csrf.CsrfViewMiddleware",
#     "django.contrib.auth.middleware.AuthenticationMiddleware",
#     "-----------vige.middleware.AuthRequiredMiddleware-----------------",
#     "django.contrib.messages.middleware.MessageMiddleware",
#     "django.middleware.clickjacking.XFrameOptionsMiddleware",
# ]
