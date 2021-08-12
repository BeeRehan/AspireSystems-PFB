from django.shortcuts import render,redirect
# Create your views here.
from django.http import HttpResponse
from testApp.form import FormProductForm
from .models import Products

def index(request):
    product = FormProductForm(request.POST or None)
    if product.is_valid():
        product.save()
        return redirect('/show')  
    return render(request,"index.html",{'form':product})
    
def show(request):  
    products = Products.objects.all()  
    return render(request,"show.htm",{"things":products}) 
