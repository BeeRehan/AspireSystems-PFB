from django.urls import path
from . import views

urlpatterns = [
    path('index',views.index, name='doctor.index'),
    path('checklist',views.checklist, name='doctor.checklist'),
    path('approval/<int:pk>',views.approval, name='doctor.approval')
]
