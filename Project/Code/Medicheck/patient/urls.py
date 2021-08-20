from django.urls import path
from . import views

urlpatterns = [
    path('appoinment',views.appoinment, name='patient'),
    path('index',views.index, name='patient.index'),
]