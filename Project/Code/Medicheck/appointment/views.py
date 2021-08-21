import appointment
from patient.views import appoinment
from django.shortcuts import render
from .models import AppoinmentDetails
# Create your views here.
def pat_detail(request,pk):
    title = "Appoinment Details"
    appoinment = AppoinmentDetails.objects.get(id=pk)
    print("Appoinment",appointment)
    return render(request,"pat_appoinment_details.html",{'title':title,'appoinment':appoinment})