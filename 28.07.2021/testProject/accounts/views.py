from django import forms
from rest_framework import views
from accounts.models import UserInfo
from django.core.checks import messages
from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.core.exceptions import *  
from testApp.views import *
from .models import UserInfo
from .form import UserRegistrationForm,UserLoginForm

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s: %(levelname)s->%(message)s")
file_handeler = logging.FileHandler("testApp.log")
file_handeler.setLevel(logging.INFO)
file_handeler.setFormatter(formatter)
err_formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
err_file_handeler = logging.FileHandler("testApp.log")
err_file_handeler.setLevel(logging.ERROR)
err_file_handeler.setFormatter(formatter)
logger.addHandler(file_handeler)
logger.addHandler(err_file_handeler)

def register(request):
    title = "Register Here"
    users = UserRegistrationForm(request.POST)
    return render(request,"register.html",{'form':users,'title':title}) 

def add_user(request):
    users = UserRegistrationForm(request.POST)
    if request.method == 'POST':
        print("Hi")
        if users.is_valid():
            print("valid")
            fname = users.cleaned_data['firstName'] 
            lname = users.cleaned_data['lastName'] 
            email = users.cleaned_data['email'] 
            username = users.cleaned_data['username']
            password = users.cleaned_data['password'] 
            password1 = users.cleaned_data['password1']
            gender = users.cleaned_data['gender']
            dob = users.cleaned_data['dob']
            bio = users.cleaned_data['bio']
            
            if(password==password1):
                user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname)
                user.save()
                userInf = UserInfo.objects.create(gender=gender,dob=dob,bio=bio,user_id=user.id)
                userInf.save()
                messages.info(request,"User Created!!!")
                logger.info(f"User {user.username} Created!!!")
                # print("Use")
                return redirect('login')
            else:
                messages.info(request,"Passwords doesn't match")
    else:
        messages.info(request,"Invalid inputs")

def login(request):
    title = "Login"
    form = UserLoginForm(request.POST)
    return render(request,'loginform.html',{'form':form,'title':title})  

def authenticate_user(request):
    form = UserLoginForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                print('Login')
                logger.info(f"User {username} logged in!!!")
                return redirect("/testApp/show")
            else:
                messages.info(request,"Invalid Login")
                return redirect('login')
        else:
            messages.info(request,"Invalid credentials!!!")
    else:
        messages.info(request,"Not a post request!!!")
        logger.error("Not a post request!!!")

def logout(request):
    auth.logout(request)
    logger.info(f"User loggedout!!!")
    return redirect('login')
