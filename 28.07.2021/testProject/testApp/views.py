from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from testApp.form import FormProductForm
from .models import Products
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import MethodMapper, api_view
from rest_framework.response import Response
from .serializers import ProductsSerializer
from django.core.exceptions import *
import pdb
from testApp import serializers

def index(request):
    return render(request,"home.html")
        

@login_required(login_url='/accounts/login')
def insert(request):
    product = FormProductForm()
    return render(request,"index.html",{'form':product})

def add_product(request):
    product = FormProductForm(request.POST or None)
    if request.method == 'POST':
        if product.is_valid():
            product.save()
            return redirect('/testApp/show')
        else:
            print("Not added!!")  

@login_required(login_url='/accounts/login')
def show(request): 
    try: 
        products = Products.objects.all()  
    except NameError:
        return HttpResponse("Object Doesn't Exist")
    return render(request,"show.htm",{"things":products}) 

@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        products = Products.objects.all()
        serializer = ProductsSerializer(products,many=True)
        return Response(serializer.data)

@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        serializers = ProductsSerializer(data=request.data)
        # pdb.set_trace()
        if serializers.is_valid():
            serializers.save()
        return HttpResponse("Inserted Successfully!!!")
    
