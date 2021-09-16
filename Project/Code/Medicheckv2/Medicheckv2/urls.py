
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.get_homepage,name="get_homepage"),
    path('admin/', admin.site.urls),
    path('appointment/',include('appointment.urls'),name="appoinment"),
    path('checkup/',include('checkup.urls'),name="checkup"),
    path('users/',include('users.urls'),name="users"),
]
