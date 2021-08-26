
from django.contrib import admin
from django.urls import path,include

from . import views
urlpatterns = [
    path('',views.index,name='Loginpage'),
    path('admin/', admin.site.urls),
    path('authenticate_user',views.authenticate_user,name='authenticate_user'),
    path('logout',views.logout,name='logout'),
    path('appointment/',include('appointment.urls'),name="appoinment"),
    path('checkup/',include('checkup.urls'),name="checkup"),
    path('users/',include('users.urls'),name="users"),
]
