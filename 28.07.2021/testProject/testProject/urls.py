from django.contrib import admin
from django.urls import include, path
from testApp import views

urlpatterns = [
    path('testApp/', include('testApp.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index),  
    path('show/',views.show),
]