from django.urls import path
from . import views

urlpatterns = [
    path('createChecklist',views.createChecklist, name='checklist.createChecklist'),
]