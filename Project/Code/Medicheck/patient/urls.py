from django.urls import path
from . import views

urlpatterns = [
    path('appoinment',views.appoinment, name='patient'),
    path('index',views.index, name='patient.index'),
    path('apply_appoinment',views.apply_appoinment, name='patient.apply_appoinment'),
    path('get_details/<int:pk>/<int:ak>',views.get_details,name='patient.get_details')
]