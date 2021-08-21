from django.urls import path
from . import views

urlpatterns = [
    path('appoinment',views.appoinment, name='patient'),
    path('index',views.index, name='patient.index'),
    path('apply_appoinment',views.apply_appoinment, name='patient.apply_appoinment'),
]