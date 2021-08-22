from django.urls import path
from . import views

urlpatterns = [
    path('createChecklist',views.createChecklist, name='checklist.createChecklist'),
    path('add_checklist/<int:pk>',views.add_checklist, name='checklist.add_checklist'),
    path('view_checklist/<int:pk>',views.view_checklist, name='checklist.view_checklist'),
]