from django.contrib import messages
from django.contrib.auth.decorators import login_required
import appointment
from patient.views import appoinment
from django.shortcuts import redirect, render
from .models import AppoinmentDetails
from .form import ApprovalForm
# Create your views here.
@login_required(login_url='/')
def approve(request,pk):
    appoinment = AppoinmentDetails.objects.get(id=pk)
    print(appoinment.status)
    appoinment.status = "approved"
    appoinment.save()
    return redirect('/doctor/index')

@login_required(login_url='/')
def reject(request,pk):
    try:
        appoinment = AppoinmentDetails.objects.get(id=pk)
        print(appoinment.status)
        appoinment.status = "rejected"
        appoinment.save()
        return redirect('/doctor/index')
    except Exception:
        messages.info(request,"Object not found")
        return redirect('/doctor/index')

@login_required(login_url='/')
def doc_detail(request,pk):
    title = "Docor Appoinment Details"
    appoinment = AppoinmentDetails.objects.get(id=pk)
    form = ApprovalForm()
    #print("Appoinment",appointment)
    return render(request,"doc_appoinment_details.html",{'title':title,'appoinment':appoinment,'form':form})
