from django.urls import path
from . import views

urlpatterns = [
    path('appoinment',views.index, name='patient'),
]