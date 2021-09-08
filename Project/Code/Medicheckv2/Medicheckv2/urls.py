
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("",views.get_homepage,name="get_homepage"),
    path('admin/', admin.site.urls),
    path('appointment/',include('appointment.urls'),name="appoinment"),
    path('checkup/',include('checkup.urls'),name="checkup"),
    path('users/',include('users.urls'),name="users"),
    #path('username_index',views.username_index,name="username_index"),
#path('check_username',views.check_username,name="check_username"),
]
