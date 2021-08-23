from django.shortcuts import redirect, render
from appointment.models import AppoinmentDetails
from .models import CheckupDetails
from .form import checklistForm
# Create your views here.
def createChecklist(request):
    apps = AppoinmentDetails.objects.filter(status="approved")
    #print(apps.id)
    return render(request,"checklist.html",{'apps':apps})

def view_checklist(request,pk):
    title = "Add Report"
    form = checklistForm()
    return render(request,"to_add_checklist.html",{'title':title,'form':form,"pk":pk}) 

def add_checklist(request,pk):
    form = checklistForm(request.POST)
    if request.method == 'POST':
        if(form.is_valid()):
            temp = form.cleaned_data['temprature']
            sugar = form.cleaned_data['sugar_level']
            bp = form.cleaned_data['bp_level']
            advice  =form.cleaned_data['advice']
            prescription = form.cleaned_data['prescription']
            deseas = form.cleaned_data['con_deseas']
            check = CheckupDetails.objects.create(temprature=temp,sugar_level=sugar,bp_level=bp,Advice=advice,prescription=prescription,confirmed_diseases=deseas,appointment_id=pk)
            check.save()
            return redirect('/checkup/createChecklist')
        else:
            print("Not valid")
    else:
        print("Not a post request") 

def doc_get_checklis(request,pk):
    apps = AppoinmentDetails.objects.filter(user_id=pk,status="approved")
    print("apps",apps)
    return render(request,"detail_appoinment.html",{'apps':apps})


def pat_get_checklis(request,pk):
    checks = CheckupDetails.objects.get(appointment_id=pk)
    return render(request,"show_checklist.html",{"checks":checks})
