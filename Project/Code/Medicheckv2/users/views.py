from django import forms
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,Group
from django.shortcuts import redirect, render
from .form import CreateUsersForm, ForgotPasswordForm, PatientDetails,PasswordResetForm
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
from .models import UserProfile
from appointment.form import ApprovalForm
from django.contrib import auth 
from .form import UserLoginForm
from hashlib import sha1
# Create your views here.
#("-----------------------------------------------------------------")

def to_login(request):
    title = "Login Page"
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
                        return redirect('/appointment/patient')
                    elif(g=='doctors'):
                        return redirect('/appointment/doctor')
                    elif(g=='admins'):
                        return redirect('/users/go_admin_page')
                else:
                    messages.info(request,"Your account was blocked!!!")
                    return redirect('/users')

                # logger.info(f"User {username} logged in!!!")
            else:
                messages.info(request,"Invalid Login credentials")
                print("auth",safe_account(request))
                return redirect('/users')
        else:
            messages.info(request,"Invalid credentials!!!")
    else:
        messages.info(request,"Not a post request!!!")
        # logger.error("Not a post request!!!")

def logout(request):
    auth.logout(request)
    # logger.info(f"User loggedout!!!")
    return redirect('/users')

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
                        return redirect('/users')
                    else:
                        messages.info(request,"Password does not match")
                        return redirect('/users/password_reset')
                else:
                    messages.info(request,"Wrong Secret Key")
                    return redirect('/users/password_reset')
            else:
                messages.info(request,"User not found")
                return redirect('/users/password_reset')
        else:
            messages.info(request,"Not valid")
            return render(request,"password_reset.html",{'form':form,'title':title,'header':header})
    else:
        messages.info(request,"Not a post")

@login_required(login_url='/users')
def go_admin_page(request):
    title = "Admin"
    users = User.objects.all()
    # print(users[1].groups[0].name)
    return render(request,"admin.html",{'title':title,'users':users})

@login_required(login_url='/users')
def create_user(request):
    form = CreateUsersForm()
    title = 'Create User'
    header = 'Create User Here!!!'
    return render(request,"create_user.html",{'form':form,'title':title,"header":header})

@login_required(login_url='/users')
def to_create_user(request):
    form = CreateUsersForm(request.POST)
    title = 'Create User'
    header = 'Create User Here!!!'
    if request.method == 'POST':
        print(request.POST['sname'])
        print(request.POST['new_password'])
        print(request.POST['group'])
        if(form.is_valid()):
            form.save()
            messages.info(request,"User Created Successfully!!!")
            return redirect('/users/go_admin_page')
        else:
            messages.info(request,"Not Valid!!!")
            return render(request,"create_user.html",{'form':form,'title':title,"header":header})
    else:
        messages.info(request,"Not a POST request!!!")
        return render(request,"create_user.html",{'form':form,'title':title,"header":header})

@login_required(login_url='/users')
def show_user_profile(request):
    title = request.user
    userdata = UserProfile.objects.get(user_id=request.user.id)
    header = f"Hi {title}"
    groups = request.user.groups.all()[0]
    print(groups)
    form = CreateUsersForm(initial={'sname':request.user,'age':userdata.age,'secret_key':userdata.secret_key})
    return render(request,"userprofile.html",{'form':form,'title':title,'header':header,'userdata':userdata,'groups':groups}) 


@login_required(login_url='/users')
def reset_user_profile(request):
    userdata = UserProfile.objects.get(user_id=request.user.id)
    user = User.objects.get(id=request.user.id)
    form = CreateUsersForm()
    userdata = UserProfile.objects.get(user_id=request.user.id)
    if(request.method == 'POST'):
        print(request.POST['sname'])
        print(request.POST['age'])
        print(request.POST['secret_key'])
        user.username = request.POST['sname']
        userdata.secret_key = request.POST['secret_key']
        userdata.age = request.POST['age']
        user.save()
        userdata.save()
        return redirect('/users/show_user_profile')
    else:
        messages.info(request,"Not a post method")
        return redirect('/users/show_user_profile')
        
@login_required(login_url='/users')
def to_delete_user(request,pk):
    user_profle = UserProfile.objects.get(user_id=pk)
    user_profle.delete()    
    user = User.objects.get(id=pk)
    user.delete()
    return redirect('/users/go_admin_page')

def show_forgot_password_form(request):
    title = 'Forgot Password'
    header = 'To Reset Password'
    form = ForgotPasswordForm()
    return render(request,"forgot_pwd.html",{'form':form,'title':title,'header':header})

def to_reset_password(request):
    form = ForgotPasswordForm(request.POST)
    title = 'Forgot Password'
    header = 'To Reset Password'
    user = User.objects.get(id=request.user.id)
    if request.method == 'POST':
        print(request.POST['crtpwd'])
        print(request.POST['newpwd'])
        print(request.POST['repwd'])
        if form.is_valid():
            print("POST")
            password = user.password
            print(password)
            
            crtpassword = form.cleaned_data['crtpwd']
            print("current",make_password(crtpassword))
            newpassword = form.cleaned_data['newpwd']
            repassword = form.cleaned_data['repwd']

            if(crtpassword == password):
                if(newpassword==repassword):
                    user.password = make_password(newpassword)
                    messages.info("Password chenged!")
                    return redirect("/users/logout")
                else:
                    messages.info(request,"Both password must be same!!!")
                    print("POST1")
                    return render(request,"forgot_pwd.html",{'form':form,'title':title,'header':header})
            else:
                messages.info(request,"current password is wrong!!!")
                print("POST2")
                return render(request,"forgot_pwd.html",{'form':form,'title':title,'header':header})
        else:
            messages.info(request,"Not valid!")
            print("POST3")
            return render(request,"forgot_pwd.html",{'form':form,'title':title,'header':header})
    else:
        messages.info(request,"Not a post method!")
        print("POST4")
        return render(request,"forgot_pwd.html",{'form':form,'title':title,'header':header})
        