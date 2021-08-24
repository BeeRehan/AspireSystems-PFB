from doctor import form
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
from appointment.form import ApprovalForm
# Create your views here.

@login_required(login_url='/')
def index(request):
    title = "Doctor page"
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(doctor=user)
    return render(request,"doc_homepage.html",{'title':title,'appoinments':appoinments,'user':user})

@login_required(login_url='/')
def checklist(request):
    title = "checklist"
    return render(request,"checklist.html",{'title':title})

@login_required(login_url='/')
def approval(request,pk):
    apps = AppoinmentDetails.objects.get(id=pk)
    form = ApprovalForm(request.POST)
    if(request.method =='POST'):
        if(form.is_valid()):
            print(apps.id)
            print(apps.status)
            apps.status = form.cleaned_data['status']
            print(apps.status)
            apps.save()
            return redirect(f'/appointment/doc_appoinnment_details/{apps.id}')
        else:
            print("Not valid")
    else:
        print("Not a post request")
