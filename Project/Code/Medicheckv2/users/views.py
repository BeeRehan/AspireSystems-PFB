from django import forms
from django.contrib.auth.models import User
from django.http.response import Http404, HttpResponse
from django.shortcuts import redirect, render
from .form import PatientDetails
from django.contrib.auth.decorators import login_required
from appointment.models import AppoinmentDetails
from .models import UserProfile
from appointment.form import ApprovalForm
# Create your views here.

@login_required(login_url='/')
def pat_homepage(request):
    form = PatientDetails()
    title = 'Patient Page'
    user = request.user
    appoinments = AppoinmentDetails.objects.filter(user_id=request.user).values()
   # print(appoinments)
    return render(request,"pat_homepage.html",{'form':form,'title':title,'appoinments':appoinments,'user':user})

@login_required(login_url='/')
def apply_appoinment(request):
    title = 'Appoinment'
    header = 'Appoinment Form'
    userdata = UserProfile.objects.get(user_id=request.user.id)
    form = PatientDetails(request.POST,request.FILES,initial={'name':request.user,'age':userdata.age,'gender':userdata.gender,'header':header})
    if request.method=='POST':
        if form.is_valid():
            form.save(request)
            return redirect('/users/patient')
        else:
            title = 'Appoinment'
            return render(request,"appoinment_form.html",{'form':form,'title':title,'header':header})
    else:
        print("Not a POST request")         

@login_required(login_url='/')
def get_details(request,pk,ak):
    title = "User Details"
    header = "User Details"
    detail = UserProfile.objects.get(user_id=pk)
    appsdet = AppoinmentDetails.objects.get(id=ak)
    # print(detail.user_id)
    user = User.objects.get(id=detail.user_id)
    print("Name",user)
    return render(request,'patient_details.html',{'detail':detail,'user':user,'appsdet':appsdet,
    'title':title,'header':header})

@login_required(login_url='/')
def appoinment(request):
    title = 'Appoinment'
    header = 'Appoinment Form'
    userdata = UserProfile.objects.get(user_id=request.user.id)
    form = PatientDetails(initial={'name':request.user,'age':userdata.age,'gender':userdata.gender})
    return render(request,"appoinment_form.html",{'form':form,'title':title,'header':header})

@login_required(login_url='/')
def doc_homepage(request):
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