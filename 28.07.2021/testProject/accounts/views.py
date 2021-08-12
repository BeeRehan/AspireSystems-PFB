from accounts.models import UserInfo
from django.core.checks import messages
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth    
from testApp.views import *
from .models import UserInfo
import re

def register(request):
    if request.method == 'POST':
        fname = request.POST['fname'] 
        lname = request.POST['lname'] 
        email = request.POST['email'] 
        username = request.POST['userid']
        password = request.POST['password'] 
        password1 = request.POST['password1']
        gender = request.POST['gender']
        dob = request.POST['dob']
        isAdmin = request.POST['admin']

        print(isAdmin)

        if re.search("[A-Za-z0-9@#$%^&+=]{8,}",password) and password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username taken")
                return redirect('register')
            elif re.search("\S+@\S+\.\S+",email) and User.objects.filter(email=email).exists():
                messages.info(request,"Email taken or wrong emailID")
                return redirect('register')
            else:    
                user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname, is_superuser=int(isAdmin))
                user.save()
                userInf = UserInfo.objects.create(gender=gender,dob=dob,user_id=user.id)
                userInf.save()
                messages.info(request,"User Created!!!")
                print("Use")
                return redirect('register')
        else:
            messages.info(request,"Password not amtching!!!")
        return redirect('register')
    return render(request,"registration.html") 

def login(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password,)

        if user is not None:
            auth.login(request,user)
            print('Login')
            return redirect("/show")
        else:
            messages.info(request,'login.html')
            return redirect('login')
    else:
        return render(request,'login.html')  

def logout(request):
    auth.logout(request)
    return redirect('login')