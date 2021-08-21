from django.urls import path
from . import views

urlpatterns = [
    path('appoinnment_details/<int:pk>',views.pat_detail, name='appoinnment_details'),
]