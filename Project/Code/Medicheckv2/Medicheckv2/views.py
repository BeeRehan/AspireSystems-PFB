from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages, auth
from users.models import UserProfile

# Create your views here.
def get_homepage(request):
    title = "Home page"
    return render(request, "homepage.html", {"title": title})
