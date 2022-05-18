from __future__ import print_function
import json
from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework import mixins,status
from rest_framework.generics import GenericAPIView,ListAPIView
from .serializer import ProductSerializer,SiginSerializer
from .models import Products, UserProfile
from rest_framework.permissions import IsAuthenticated,AllowAny
from e_backend.settings import GRANT_TYPE
# Create your views here.
class ApiClass(ListAPIView):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        AllowAny,
    ]

class SignInView(GenericAPIView):
    serializer_class = SiginSerializer
    permission_classes = [
        AllowAny,
    ]

    def post(self,request):
        serializer = self.get_serializer(data=request.data)

        if(serializer.is_valid()):
            data = {
                "grant_type" : GRANT_TYPE,
                "username" : request.data['username'],
                "password" : request.data['password'],
                "client_id" : request.data['client_id'],
                "client_secret" : request.data['client_secret']
            }
            token_info = requests.post("http://127.0.0.1:8000/o/token/",data=data)
            token_info = json.loads(token_info.content)
            print(token_info)
            if("error" in token_info):
                return Response(data=token_info['error_description'],status=status.HTTP_400_BAD_REQUEST)
        
            return Response(status=status.HTTP_200_OK,data=token_info)

from django.contrib.auth.models import User
from .models import UserProfile

class SignupView(GenericAPIView):
    permission_classes = [AllowAny]
    
    def post(self,request):
        try:
            user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'])
            user.save()
        except Exception as e:
            print(json(e))
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        try:
            profile = UserProfile.objects.create(age=request.POST['age'],address=request.POST['address'])
            profile.save()
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST,data=e)
        return Response(status=status.HTTP_201_CREATED,data=json.dumps("Signup Successfull"))