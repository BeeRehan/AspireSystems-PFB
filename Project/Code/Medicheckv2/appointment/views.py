from typing import get_origin
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render, HttpResponse
from .models import AppoinmentDetails
from .form import ApprovalForm
from users.form import PatientDetails
from users.models import UserProfile
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import AppoimentSerializer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime


@api_view(["GET"])
# @login_required(login_url='/users')
def api_get_patient(request):
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user.id)
    serializer = AppoimentSerializer(appoinments, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def api_get_patientt(request):
    
    #print(dir(request))
    token = request.headers.get('Authorization')
    #print(token)

    if not token:
        raise AuthenticationFailed('Unauthenticated!')

    try:
        payload = jwt.decode(token, 'secret', algorithms=['HS256'])
    
    except jwt.ExpiredSignatureError:
        raise AuthenticationFailed('Unauthenticated!')

    appoinments = AppoinmentDetails.objects.filter(user_id=payload['id'])
    serializer = AppoimentSerializer(appoinments, many=True)
    return Response(serializer.data)


def api_doc_homepage(request):
    title = "Doctor page"
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(doctor=user)
    appoinments_list = []
    for appoinment in appoinments:
        name = User.objects.get(id=appoinment.user_id).username
        appoinments_list.append(
            dict(
                id=appoinment.id,
                date=appoinment.date,
                status=appoinment.status,
                name=name,
            )
        )
    # print(appoinments_list)
    return render(
        request,
        "doc_homepage.html",
        {"title": title, "appoinments": appoinments_list, "user": user},
    )

@api_view(["POST"])
def api_patient_post_checklist(request):
    serializers = AppoimentSerializer(data=request.data)
    if request.method == "POST":
        if serializers.is_valid():
            serializers.save()
            return HttpResponse("Inserted Successfully!!!")
    else:
        return HttpResponse("Not a post request!!!")


@login_required(login_url="/users")
def approve(request, pk):
    try:
        appoinment = AppoinmentDetails.objects.get(id=pk)
        appoinment.status = "approved"
        appoinment.save()
        return redirect("/appointment/doctor")
    except Exception:
        messages.info(request, "No object")
        return redirect("/appointment/doctor")


@login_required(login_url="/users")
def reject(request, pk):
    try:
        appoinment = AppoinmentDetails.objects.get(id=pk)
        appoinment.status = "rejected"
        appoinment.save()
        return redirect("/appointment/doctor")
    except Exception:
        messages.info(request, "Object not found")
        return redirect("/appointment/doctor")


@login_required(login_url="/users")
def doc_detail(request, pk):
    title = "Docor Appoinment Details"
    appoinment = AppoinmentDetails.objects.get(id=pk)
    form = ApprovalForm()
    # print("Appoinment",appointment)
    return render(
        request,
        "doc_appoinment_details.html",
        {"title": title, "appoinment": appoinment, "form": form},
    )


@login_required(login_url="/users")
def pat_homepage(request):
    form = PatientDetails()
    title = "Patient Page"
    # header = 'Welcome to Patient page!!!!'
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user).values()
    # print(appoinments)
    return render(
        request,
        "pat_homepage.html",
        {"form": form, "title": title, "appoinments": appoinments, "user": user,},
    )


@login_required(login_url="/users")
def apply_appoinment(request):
    title = "Appoinment"
    header = "Appoinment Form"
    userdata = UserProfile.objects.get(user_id=request.user.id)
    form = PatientDetails(
        request.POST,
        request.FILES,
        initial={"name": request.user, "age": userdata.age, "gender": userdata.gender},
    )
    if request.method == "POST":
        if form.is_valid():
            form.save(request)
            return redirect("/appointment/patient")
        else:
            title = "Appoinment"
            return render(
                request,
                "appoinment_form.html",
                {"form": form, "title": title, "header": header},
            )
    else:
        print("Not a POST request")


@login_required(login_url="/users")
def get_details(request, pk, ak):
    title = "User Details"
    header = "User Details"
    detail = UserProfile.objects.get(user_id=pk)
    appsdet = AppoinmentDetails.objects.get(id=ak)
    # print(detail.user_id)
    user = User.objects.get(id=detail.user_id)
    print("Name", user)
    return render(
        request,
        "patient_details.html",
        {
            "detail": detail,
            "user": user,
            "appsdet": appsdet,
            "title": title,
            "header": header,
        },
    )


@login_required(login_url="/users")
def appoinment(request):
    title = "Appoinment"
    header = "Appoinment Form"
    userdata = UserProfile.objects.get(user_id=request.user.id)
    form = PatientDetails(
        initial={"name": request.user, "age": userdata.age, "gender": userdata.gender}
    )
    return render(
        request,
        "appoinment_form.html",
        {"form": form, "title": title, "header": header},
    )


@login_required(login_url="/users")
def doc_homepage(request):
    title = "Doctor page"
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(doctor=user)
    appoinments_list = []
    for appoinment in appoinments:
        name = User.objects.get(id=appoinment.user_id).username
        appoinments_list.append(
            dict(
                id=appoinment.id,
                date=appoinment.date,
                status=appoinment.status,
                name=name,
            )
        )
    # print(appoinments_list)
    return render(
        request,
        "doc_homepage.html",
        {"title": title, "appoinments": appoinments_list, "user": user},
    )


@login_required(login_url="/users")
def checklist(request):
    title = "checklist"
    return render(request, "checklist.html", {"title": title})


@login_required(login_url="/users")
def approval(request, pk):
    apps = AppoinmentDetails.objects.get(id=pk)
    form = ApprovalForm(request.POST)
    if request.method == "POST":
        if form.is_valid():
            print(apps.id)
            print(apps.status)
            apps.status = form.cleaned_data["status"]
            print(apps.status)
            apps.save()
            return redirect(f"/appointment/doc_appoinnment_details/{apps.id}")
        else:
            messages.info(request, "Not valid")
            print("Not valid")
    else:
        print("Not a post request")
