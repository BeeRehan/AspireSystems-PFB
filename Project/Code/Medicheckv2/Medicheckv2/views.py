from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from .form import UserLoginForm,PasswordResetForm
from django.contrib.auth.models import User
from django.contrib import messages,auth
from users.models import UserProfile

def reset(request):
    name = User.objects.get(username=request.POST['username'])
    user = UserProfile.objects.get(user_id=name.id)
    user.attempt = 0
    user.save()

def safe_account(request):
    name = User.objects.get(username=request.POST['username'])
    user = UserProfile.objects.get(user_id=name.id)
    user.attempt += 1
    if(user.attempt == 3):
        user.account_status='blocked'
    user.save()

def username_index(request):
    form  = UserLoginForm()
    header = "Enter Username here"
    title = "Password Reset Form"
    return render(request,"getusername.html",{'form':form,'title':title,'header':header})

def check_username(request):
    form = UserProfile()
    if(request.method=='POST'):
        user = User.objects.get(username=request.POST['username'])
        if(user):
            return redirect(f'/password_reset/{user.id}')
        else:
            messages.info(request,"User not exists")
            return render(request,"username.html",{'form':form})
    else:
        print("Not a post request")

def password_reset(request):
    form = PasswordResetForm()
    header = "Password Reset Form"
    title = "Password Reset Form"
    return render(request,"password_reset.html",{'form':form,'title':title,'header':header})

def password_reseter(request):
    form = PasswordResetForm(request.POST)
    header = "Password Reset Form"
    title = "Password Reset Form"
    if(request.method=='POST'):
        if(form.is_valid()):
            username = form.cleaned_data['username']
            key = form.cleaned_data['key']
            new_password = form.cleaned_data['new_password']
            con_password = form.cleaned_data['con_password']
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user_id=user.id)
            if(user):
                if(user_profile.secret_key==key):
                    if(new_password==con_password):
                        form.save(user.id)
                        messages.info(request,"Unlocked Successfully")
                        return redirect('/')
                    else:
                        messages.info(request,"Password does not match")
                else:
                    messages.info(request,"Wrong Secret Key")
            else:
                messages.info(request,"User not found")
        else:
            messages.info(request,"Not valid")
            return render(request,"password_reset.html",{'form':form,'title':title,'header':header})
    else:
        messages.info(request,"Not a post")

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
                    reset(request)
                    g = request.user.groups.all()[0].name
                    print("=>",g)
                    if(g=='patients'):
                        return redirect('users/patient')
                    elif(g=='doctors'):
                        return redirect('users/doctor')
                else:
                    messages.info(request,"Your account was blocked!!!")
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
