from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .form import UserLoginForm
from django.contrib.auth.models import User
from django.contrib import messages,auth
from users.models import UserProfile

def safe_account(request):
    name = User.objects.get(username=request.POST['username'])
    user = UserProfile.objects.get(user_id=name.id)
    user.attempt += 1
    if(user.attempt == 3):
        user.account_status='blocked'
    user.save()
# Create your views here.
def index(request):
    title = "Homepage"
    form = UserLoginForm()
    print("Page")
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
                if(not UserProfile.objects.get(user_id=user.id).account_status=='blocked'):
                    print("passed")
                    g = request.user.groups.all()[0].name
                    print("=>",g)
                    if(g=='patients'):
                        return redirect('users/patient')
                    elif(g=='doctors'):
                        return redirect('users/doctor')
                else:
                    messages.info(request,"Your account was blocked \n Contact your admin team!!!")
                    return redirect('/')

                # logger.info(f"User {username} logged in!!!")
            else:
                messages.info(request,"Invalid Login credentials")
                print("auth",safe_account(request))
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
