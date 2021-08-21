from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
# Create your views here.

@login_required(login_url='/')
def index(request):
    title = "Doctor page"
    user = request.user
    appoinments = AppoinmentDetails.objects.filter  (doctor=user)
    return render(request,"doc_homepage.html",{'title':title,'appoinments':appoinments,'user':user})

@login_required(login_url='/')
def checklist(request):
    title = "checklist"
    return render(request,"checklist.html",{'title':title})

def approval(request,pk):
    apps = AppoinmentDetails.objects.get(id=pk)