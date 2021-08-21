from django.contrib.auth.models import User
from django.shortcuts import render
from .form import PatientDetails
from appointment.models import AppoinmentDetails
# Create your views here.

def index(request):
    form = PatientDetails()
    title = 'Patient Page'
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user).values()
    print(appoinments)
    return render(request,"pat_homepage.html",{'form':form,'title':title,'appoinments':appoinments})

def appoinment(request):
    title = 'Appoinment Form'
    form = PatientDetails()

    return render(request,"appoinment_form.html",{'form':form,'title':title})