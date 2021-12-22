from django.shortcuts import render
from rest_framework import serializers
from .models import UserProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UserProfileSerializer
# Create your views here.

@api_view(['GET'])
def list_urls(request):
    urls = {
        "List":"rest-list",
        "Create":"rest-create",
        "Get":"rest-get/<str:pk>",
        "Update":"rest-update/<str:pk>",
        "Delete":"rest-delete/<str:pk>",
    }
    return Response(urls)


@api_view(['GET'])
def list_data(request):
    users = UserProfile.objects.all()
    serializer = UserProfileSerializer(users,many=True)
    
    return Response(serializer.data)

@api_view(['POST'])
def insert_data(request):
    serializer = UserProfileSerializer(data=request.data)
    if(serializer.is_valid()):
        message = "Inserted Successfull"
        serializer.save()
    else:
        message = "Inserted Unsuccessfull"
    
    return Response(message)  


@api_view(['GET'])
def get_data(request,pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(user)    
    return Response(serializer.data)

@api_view(['POST'])
def update_data(request,pk):
    user = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(instance=user,data=request.data)
    if(serializer.is_valid()):
        message = "Upadeted Successfull"
        serializer.save()
    else:
        message = "Upadeted Unsuccessfull"
    
    return Response(message)

@api_view(['DELETE'])
def delete_data(request,pk):
    users = UserProfile.objects.get(id=pk)
    users.delete()
    message = "Upadeted Successfull"
    return Response(message)    
