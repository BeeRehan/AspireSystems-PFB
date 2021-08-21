import appointment
from patient.views import appoinment
from django.shortcuts import render
from .models import AppoinmentDetails
from .form import ApprovalForm
# Create your views here.
def pat_detail(request,pk):
    title = "Patient Appoinment Details"
    appoinment = AppoinmentDetails.objects.get(id=pk)
    #print("Appoinment",appointment)
    return render(request,"pat_appoinment_details.html",{'title':title,'appoinment':appoinment})

def doc_detail(request,pk):
    title = "Docor Appoinment Details"
    appoinment = AppoinmentDetails.objects.get(id=pk)
    form = ApprovalForm()
    #print("Appoinment",appointment)
    return render(request,"doc_appoinment_details.html",{'title':title,'appoinment':appoinment,'form':form})