from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User


class MIDDLEWARE:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            messages.info(request, "Login Required!!!")
            return redirect(request, "/users")
