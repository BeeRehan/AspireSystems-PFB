from django import forms
from accounts.models import UserInfo
from django.core.checks import messages
from django.contrib import messages,auth
from django.shortcuts import redirect, render
from django.contrib.auth.models import User    
from testApp.views import *
from .models import UserInfo
from .form import UserRegistrationForm,UserLoginForm

def register(request):
    title = "Register Here"
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
            #isAdmin = users.cleaned_data['admincheck']
            #print(isAdmin)

            if(password==password1):
                user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname)
                user.save()
                userInf = UserInfo.objects.create(gender=gender,dob=dob,bio=bio,user_id=user.id)
                userInf.save()
                messages.info(request,"User Created!!!")
                print("Use")
                return redirect('login')
            else:
                messages.info(request,"Passwords doesn't match")
        else:
            messages.info(request,"Invalid inputs")
    return render(request,"register.html",{'form':users,'title':title}) 

def login(request):
    title = "Login"
    form = UserLoginForm(request.POST)
    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                print('Login')
                #if request.user.is_authenticated:
                return redirect("/show")
            else:
                messages.info("Invalid Login")
                return redirect('login')
    else:
        return render(request,'loginform.html',{'form':form,'title':title})  

def logout(request):
    auth.logout(request)
    return redirect('login')


# if request.method == 'POST':
    #if form.is_valid:
#         fname = request.POST['fname'] 
#         lname = request.POST['lname'] 
#         email = request.POST['email'] 
#         username = request.POST['userid']
#         password = request.POST['password'] 
#         password1 = request.POST['password1']
#         gender = request.POST['gender']
#         dob = request.POST['dob']
#         isAdmin = request.POST['admin']
#         print(isAdmin)

#         if re.search("[A-Za-z0-9@#$%^&+=]{8,}",password) and password==password1:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,"Username taken")
#                 return redirect('register')
#             elif re.search("\S+@\S+\.\S+",email) and User.objects.filter(email=email).exists():
#                 messages.info(request,"Email taken or wrong emailID")
#                 return redirect('register')
#             else:    
#                 user = User.objects.create_user(username=username, password=password, email=email, first_name=fname, last_name=lname, is_superuser=int(isAdmin))
#                 user.save()
#                 userInf = UserInfo.objects.create(gender=gender,dob=dob,user_id=user.id)
#                 userInf.save()
#                 messages.info(request,"User Created!!!")
#                 print("Use")
#                 return redirect('login')
#         else:
#             messages.info(request,"Password not matching!!!")
#         return redirect('register')