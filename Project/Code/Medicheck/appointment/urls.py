from django.urls import path
from . import views

urlpatterns = [
    path('pat_appoinnment_details/<int:pk>',views.pat_detail, name='pat_appoinnment_details'),
    path('doc_appoinnment_details/<int:pk>',views.doc_detail, name='doc_appoinnment_details'),
]