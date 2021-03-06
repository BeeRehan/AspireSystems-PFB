from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .form import UserLoginForm
from django.contrib.auth.models import User,Group
from django.contrib import messages,auth

# Create your views here.
def index(request):
    title = "Homepage"
    form = UserLoginForm()
    return render(request,"login.html",{'title':title ,'form':form})

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
                g = request.user.groups.all()[0].name
                print("=>",g)
                if(g=='patients'):
                   return redirect('/patient/')
                elif(g=='doctors'):
                    return redirect('/doctor/')
                # logger.info(f"User {username} logged in!!!")
            else:
                messages.info(request,"Invalid Login")
                return redirect('/')
        else:
            messages.info(request,"Invalid credentials!!!")
    else:
        messages.info(request,"Not a post request!!!")
        # logger.error("Not a post request!!!")

def logout(request):
    auth.logout(request)
    # logger.info(f"User loggedout!!!")
    return redirect('/')
