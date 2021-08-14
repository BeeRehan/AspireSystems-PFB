from django.shortcuts import render,redirect
from django.http import HttpResponse
from testApp.form import FormProductForm
from .models import Products
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductsSerializer

@login_required(login_url='/accounts/login')
def index(request):
    product = FormProductForm()
    # if product.is_valid():
    #     product.save()
    #     return redirect('/show')
    # else:
    #     print("Not added!!") 
    return render(request,"index.html",{'form':product})

def add_product(request):
    product = FormProductForm(request.POST or None)
    if request.method == 'POST':
        if product.is_valid():
            product.save()
            return redirect('/show')
        else:
            print("Not added!!")  

@login_required(login_url='/accounts/login')
def show(request):  
    products = Products.objects.all()  
    return render(request,"show.htm",{"things":products}) 

class ProductList(APIView):
    def get(self,request):
        products = Products.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)

    
