from django.contrib.auth.models import User
from django.shortcuts import render
from .form import PatientDetails
# Create your views here.

def index(request):
    form = PatientDetails()
    title = 'Patient Page'
    return render(request,"pat_homepage.html",{'form':form,'title':title})

def appoinment(request):
    title = 'Appoinment Form'
    form = PatientDetails()
    return render(request,"appoinment_form.html",{'form':form,'title':title})