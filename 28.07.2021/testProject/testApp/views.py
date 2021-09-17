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
import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s:%(name)s: %(levelname)s->%(message)s")
file_handeler = logging.FileHandler("testApp.log")
file_handeler.setLevel(logging.INFO)
file_handeler.setFormatter(formatter)
err_formatter = logging.Formatter("%(asctime)s:%(name)s:%(message)s")
err_file_handeler = logging.FileHandler("testApp.log")
err_file_handeler.setLevel(logging.ERROR)
err_file_handeler.setFormatter(formatter)
logger.addHandler(file_handeler)
logger.addHandler(err_file_handeler)


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
            logger.info("Item Inserted")
            return redirect('/testApp/show')
        else:
            logger.info("Not added!!")

@login_required(login_url='/accounts/login')
def show(request):
    try:
        products = Products.objects.all()
    except NameError:
        logger.error("Object Doesn't Exist")
        return HttpResponse("Object Doesn't Exist")
    return render(request,"show.htm",{"things":products})

@api_view(['GET'])
def get(request):
    if request.method == 'GET':
        print("Type:",request.content_type)
        if(request.content_type=="application/json"):
            products = Products.objects.all()
            serializer = ProductsSerializer(products,many=True)
            logger.info("Json Response Returned")
            return Response(serializer.data)

        elif(request.content_type=="text/plain"):
            try:
                products = Products.objects.all()
            except NameError:
                logger.error("Object Doesn't Exist")
                return HttpResponse("Object Doesn't Exist")
            return render(request,"show.htm",{"things":products})


@api_view(['POST'])
def post(request):
    if request.method == 'POST':
        if(request.content_type=="application/json"):
            serializers = ProductsSerializer(data=request.data)
            # pdb.set_trace()
            if serializers.is_valid():
                serializers.save()
                logger.info("JSON data Inserted Successfully!!!")
            return HttpResponse("Inserted Successfully!!!")
        # elif(request.content_type=="text/plain"):
        #     return redirect('insert')
