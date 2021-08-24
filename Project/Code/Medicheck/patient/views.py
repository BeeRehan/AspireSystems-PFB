from django import forms
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .form import PatientDetails
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
from .models import UserProfile
# Create your views here.

@login_required(login_url='/')
def index(request):
    form = PatientDetails()
    title = 'Patient Page'
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user).values()
   # print(appoinments)
    return render(request,"pat_homepage.html",{'form':form,'title':title,'appoinments':appoinments,'user':user})

@login_required(login_url='/')
def apply_appoinment(request):
    form = PatientDetails(request.POST,request.FILES)
    if request.method=='POST':
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            reason = form.cleaned_data['reason']
            doctor = form.cleaned_data['doctor']
            vaccinated = form.cleaned_data['vaccinated']
            file = form.cleaned_data['scan_report']
            # print(str(date)+" "+str(time))
           # user = UserProfile.objects.create(age=age,gender=gender)  
            app = AppoinmentDetails(date=(str(date)+" "+str(time)),vaccinated=vaccinated,file=file,doctor=doctor,reason=reason,status="requested",user_id=request.user.id)
            app.save()
            return redirect('/patient/index')
        else:
            print("Not Valid")
            return HttpResponse("Not Valid")
    else:
        print("Not a POST request")         

@login_required(login_url='/')
def get_details(request,pk,ak):
    detail = UserProfile.objects.get(user_id=pk)
    appsdet = AppoinmentDetails.objects.get(id=ak)
    print(detail.user_id)
    user = User.objects.get(id=detail.user_id)
    print("Name",user)
    return render(request,'patient_details.html',{'detail':detail,'user':user,'appsdet':appsdet})



@login_required(login_url='/')
def appoinment(request):
    title = 'Appoinment'
    userdata = UserProfile.objects.get(user_id=request.user.id)
    form = PatientDetails(initial={'name':request.user,'age':userdata.age,'gender':userdata.gender})
    return render(request,"appoinment_form.html",{'form':form,'title':title})