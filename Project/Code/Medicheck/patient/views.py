from django.shortcuts import render
from .form import PatientDetails
# Create your views here.

def index(request):
    form = PatientDetails()
    title = 'Patient Page'
    return render(request,"appoinment_form.html",{'form':form,'title':title})