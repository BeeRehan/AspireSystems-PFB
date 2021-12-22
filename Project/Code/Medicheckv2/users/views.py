from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User,Group
from django.http import response
from django.shortcuts import redirect, render
from rest_framework import serializers
from .form import CreateUsersForm, ForgotPasswordForm,PasswordResetForm
from django.shortcuts import redirect, render, HttpResponse
from .form import CreateUsersForm, ForgotPasswordForm, PasswordResetForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from django.contrib import auth
from .form import UserLoginForm
from .serializers import UserProfileSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
#-------------------------------------------------------------------------
'''
Admin
'''

@api_view(['GET'])
def list_data(request):
    token = request.headers.get('Authorization')
    #print(token)

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')


    users = User.objects.all()
    usersL  = []
    # print(type(list(users)),list(users),len(users))
    
    try:
        for user in  users:
            # print(user)    
            status = ""        
            if(user.is_active):
                status = "Active"
            else:
                status = "Inactive"
            usersL.append(dict(
                id=user.id,
                username=user.username,
                status=status,
                group=user.groups.all()[0].name,
                ))
    except Exception as e:
        print("List Users Error:",e)
        

    # print("E",usersL,users)
    # except Exception as e:
    #     print("E",userList,users)
    #     print(e)    
    
    return Response(usersL)


@api_view(['POST'])
def api_add_user(request):
    token = request.headers.get('Authorization')
    #print(token)

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        print("Data",request.data)
        user = User.objects.create_user(username=request.data['Username'],
                    password=request.data['Password'])
        user.save()

        profile = UserProfile.objects.create(
            user_id = user.id,
            age = request.data['Age'],
            gender = request.data['Gender'],
            secret_key = request.data['Secret Key']
        )

        profile.save()
        
        groups = Group.objects.get(name=request.data["Group"])
        groups.user_set.add(user)
        groups.save()
        
        message = "Added Succesfully!!!"
    except Exception as e :
        message = f'Added unsuccesfully with {e}'


    return Response(message)

@api_view(['DELETE'])
def api_delete_data(request,pk):
    try:
        user = User.objects.get(id=pk)
        user.delete()
        profile = UserProfile.objects.get(user_id=id)
        profile.save()
        message = "Upadeted Successfull"
    except Exception as e:
        message = f"Upadeted unsuccessfull{e}"
    
    return Response('message')

#----------------------------------------------------------------------------------
@api_view(["GET"])
# @login_required(login_url='/users')
def api_show_user_profile(request):
    token = request.headers.get('Authorization')
    #print(token)

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    deatils = UserProfile.objects.get(user_id=request.user.id)
    serializer = UserProfileSerializer(deatils)
    return Response(serializer.data)

@api_view(["GET"])
def api_get_user_profile(request):
    token = request.headers.get('Authorization')
    #print(token)

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
        
    user = User.objects.get(id=payload['id'])
    deatils = UserProfile.objects.get(user_id=payload['id'])
    # serializer = UserProfileSerializer(deatils)

    userDdetails = {
        'user_id' : user.id,
        'name':user.username,
        'age' : deatils.age,
        'group':user.groups.all()[0].name,
        'gender':deatils.gender,
        'key':deatils.secret_key
    }

    return Response(data=userDdetails)

@api_view(["POST"])
def api_post_user_profile(request):

    # print("Post User Details")

    token = request.headers.get('Authorization')

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')
    try:
        data = {
            'age' : request.data['Age'],
            'key' : request.data['Secret Key']
        }
        
        user = UserProfile.objects.get(user_id=payload['id'])
        user.age=data['age']
        user.secret_key=data['key']
        user.save()
    except Exception as e:
        print(e)
    return Response("Updated successfully")

@api_view(["POST"])
def api_register(request):
    username = request.data['username']
    password = request.data['password']
    user = User.objects.create_user(username=username,password=password)
    user.save()

    return HttpResponse("User was created")

@api_view(["GET"])
# @login_required(login_url='/users')
def api_show_user(request):
    deatils = User.objects.get(id=request.user.id)
    serializer = UserSerializer(deatils)
    return Response(serializer.data)

@api_view(["POST"])
def api_login(request):
    username = request.data['username']
    password = request.data['password']

    user = User.objects.filter(username=username).first()

    # print(user.groups.all()[0].name)
    if user is None and password is None:
        raise AuthenticationFailed("User not Found!!!")

    if not user.check_password(password):
        raise AuthenticationFailed("Incorrect Password!!!")

        
    payload = {
        'id': user.id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow(),
        'group':user.groups.all()[0].name
    }

    token = jwt.encode(payload, 'secret', algorithm='HS256')

    # token = jwt.decode(token,'utf-8',algorithms='HS256',options={"verify_signature": False})
    response = Response()
    response.set_cookie(key='jwt', value=token, httponly=True)
    
    response.data = {
        'jwt': token
    }
    
    return response

@api_view(['POST'])
def api_logout(request):
    response = Response()
    response.delete_cookie('jwt')
    response.data = {
        'message': 'success'
    }
    return response


@api_view(["POST"])
def api_post_user(request):
    serializers = UserSerializer(data=request.data)
    if request.method == "POST":
        if serializers.is_valid():
            serializers.save()
            return HttpResponse("Inserted Successfully!!!")
    else:
        return HttpResponse("Not a post request!!!")


def to_login(request):
    title = "Login Page"
    form = UserLoginForm()
    return render(request, "login.html", {"title": title, "form": form})


def authenticate_user(request):
    form = UserLoginForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)
                if (
                    not UserProfile.objects.get(user_id=user.id).account_status
                    == "blocked"
                ):
                    reset(request)
                    g = request.user.groups.all()[0].name
                    if not g == "admins":
                        return redirect(f"/appointment/{g[:-1]}")
                    else:
                        return redirect("/users/admin")
                else:
                    messages.info(request, "Your account was blocked!!!")
                    return redirect("/users")
            else:
                messages.info(request, "Invalid Login credentials")
                safe_account(request)
                return redirect("/users")
        else:
            messages.info(request, "Invalid credentials!!!")
    else:
        messages.info(request, "Not a post request!!!")


def logout(request):
    auth.logout(request)
    return redirect("/users")


def reset(request):
    name = User.objects.get(username=request.POST["username"])
    user = UserProfile.objects.get(user_id=name.id)
    user.attempt = 0
    user.save()


def safe_account(request):
    name = User.objects.get(username=request.POST["username"])
    user = UserProfile.objects.get(user_id=name.id)
    user.attempt += 1
    if user.attempt == 3:
        user.account_status = "blocked"
    user.save()


def password_reset(request):
    form = PasswordResetForm()
    header = "Password Reset Form"
    title = "Password Reset Form"
    return render(
        request, "password_reset.html", {"form": form, "title": title, "header": header}
    )


def password_reseter(request):
    form = PasswordResetForm(request.POST)
    header = "Password Reset Form"
    title = "Password Reset Form"
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data["username"]
            key = form.cleaned_data["key"]
            user = User.objects.get(username=username)
            user_profile = UserProfile.objects.get(user_id=user.id)
            if user:
                if user_profile.secret_key == key:
                    new_password = form.cleaned_data["new_password"]
                    con_password = form.cleaned_data["con_password"]
                    if new_password == con_password:
                        form.save(user.id)
                        messages.info(request, "Unlocked Successfully")
                        return redirect("/users")
                    else:
                        messages.info(request, "Password does not match")
                        return redirect("/users/password_reset")
                else:
                    messages.info(request, "Wrong Secret Key")
                    return redirect("/users/password_reset")
            else:
                messages.info(request, "User not found")
                return redirect("/users/password_reset")
        else:
            messages.info(request, "Not valid")
            return render(
                request,
                "password_reset.html",
                {"form": form, "title": title, "header": header},
            )
    else:
        messages.info(request, "Not a post")


@login_required(login_url="/users")
def go_admin_page(request):
    title = "Admin"
    users = User.objects.all()
    users_list = []
    for user in users:
        users_list.append(
            dict(
                name=user, id=user.id, group=user.groups.all()[0], status=user.is_active
            )
        )
    return render(request, "admin.html", {"title": title, "users": users_list})


@login_required(login_url="/users")
def create_user(request):
    form = CreateUsersForm()
    title = "Create User"
    header = "Create User Here!!!"
    return render(
        request, "create_user.html", {"form": form, "title": title, "header": header}
    )


@login_required(login_url="/users")
def to_create_user(request):
    form = CreateUsersForm(request.POST)
    title = "Create User"
    header = "Create User Here!!!"
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.info(request, "User Created Successfully!!!")
            return redirect("/users/admin")
        else:
            messages.info(request, "Not Valid!!!")
            return render(
                request,
                "create_user.html",
                {"form": form, "title": title, "header": header},
            )
    else:
        messages.info(request, "Not a POST request!!!")
        return render(
            request,
            "create_user.html",
            {"form": form, "title": title, "header": header},
        )


@login_required(login_url="/users")
def show_user_profile(request):
    title = request.user
    userdata = UserProfile.objects.get(user_id=request.user.id)
    header = f"Hi {title}"
    groups = request.user.groups.all()[0]
    form = CreateUsersForm(
        initial={
            "sname": request.user,
            "age": userdata.age,
            "secret_key": userdata.secret_key,
        }
    )
    return render(
        request,
        "userprofile.html",
        {
            "form": form,
            "title": title,
            "header": header,
            "userdata": userdata,
            "groups": groups,
        },
    )


@login_required(login_url="/users")
def reset_user_profile(request):
    userdata = UserProfile.objects.get(user_id=request.user.id)
    user = User.objects.get(id=request.user.id)
    userdata = UserProfile.objects.get(user_id=request.user.id)
    if request.method == "POST":
        user.username = request.POST["sname"]
        userdata.secret_key = request.POST["secret_key"]
        userdata.age = request.POST["age"]
        user.save()
        userdata.save()
        return redirect("/users/show_user_profile")
    else:
        messages.info(request, "Not a post method")
        return redirect("/users/show_user_profile")


@login_required(login_url="/users")
def to_delete_user(request, pk):
    user_profle = UserProfile.objects.get(user_id=pk)
    user_profle.delete()
    user = User.objects.get(id=pk)
    user.delete()
    return redirect("/users/admin")


@login_required(login_url="/users")
def show_forgot_password_form(request):
    title = "Forgot Password"
    header = "To Reset Password"
    form = ForgotPasswordForm()
    return render(
        request, "forgot_pwd.html", {"form": form, "title": title, "header": header}
    )


def to_reset_password(request):
    form = ForgotPasswordForm(request.POST)
    title = "Forgot Password"
    header = "To Reset Password"
    user = User.objects.get(id=request.user.id)
    if request.method == "POST":
        if form.is_valid():
            newpassword = form.cleaned_data["newpwd"]
            repassword = form.cleaned_data["repwd"]
            if newpassword == repassword:
                user.password = make_password(newpassword)
                user.save()
                messages.info(request, "Password chenged!")
                return redirect("/users/logout")
            else:
                messages.info(request, "Both password must be same!!!")
                return render(
                    request,
                    "forgot_pwd.html",
                    {"form": form, "title": title, "header": header},
                )
        else:
            messages.info(request, "Not valid!")
            return render(
                request,
                "forgot_pwd.html",
                {"form": form, "title": title, "header": header},
            )
    else:
        messages.info(request, "Not a post method!")
        return render(
            request, "forgot_pwd.html", {"form": form, "title": title, "header": header}
        )
