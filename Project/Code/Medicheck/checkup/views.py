from django.shortcuts import render
from appointment.models import AppoinmentDetails
from .form import checklistForm
# Create your views here.
def createChecklist(request):
    apps = AppoinmentDetails.objects.filter(status="approved")
    #print(apps.id)
    return render(request,"checklist.html",{'apps':apps})

def add_checklist(request):
    pass