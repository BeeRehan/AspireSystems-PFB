from django.shortcuts import render
from appointment.models import AppoinmentDetails
# Create your views here.
def index(request):
    title = "Doctor page"
    appoinments = AppoinmentDetails.objects.all()
    return render(request,"doc_homepage.html",{'title':title,'appoinments':appoinments})

def checklist(request):
    title = "checklist"
    return render(request,"checklist.html",{'title':title})
