from django.contrib.auth.models import User
from django.shortcuts import render
from .form import PatientDetails
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
# Create your views here.

@login_required(login_url='/')
def index(request):
    form = PatientDetails()
    title = 'Patient Page'
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user).values()
    print(appoinments)
    return render(request,"pat_homepage.html",{'form':form,'title':title,'appoinments':appoinments,'user':user})

@login_required(login_url='/')
def appoinment(request):
    title = 'Appoinment Form'
    form = PatientDetails()
    return render(request,"appoinment_form.html",{'form':form,'title':title})