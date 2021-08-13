from django.shortcuts import render,redirect
from django.http import HttpResponse
from testApp.form import FormProductForm
from .models import Products
from django.contrib.auth.decorators import login_required
from django.contrib import auth

@login_required(login_url='/accounts/login')
def index(request):
    product = FormProductForm(request.POST or None)
    if product.is_valid():
        product.save()
        return redirect('/show')  
    return render(request,"index.html",{'form':product})

@login_required(login_url='/accounts/login')
def show(request):  
    products = Products.objects.all()  
    return render(request,"show.htm",{"things":products}) 

def logout(request):
    auth.logout(request)
    return redirect('login')