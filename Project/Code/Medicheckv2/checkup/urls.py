from django.urls import path
from . import views

urlpatterns = [
    path('createChecklist',views.createChecklist, name='checklist.createChecklist'),
    path('add_checklist/<int:pk>',views.add_checklist, name='checklist.add_checklist'),
    path('view_checklist/<int:pk>',views.view_checklist, name='checklist.view_checklist'),
    path('pat_get_checklis/<int:pk>',views.pat_get_checklis, name='checklist.pat_get_checklis'),
    path('doc_get_checklis/<int:pk>',views.doc_get_checklis, name='checklist.doc_get_checklis')
]