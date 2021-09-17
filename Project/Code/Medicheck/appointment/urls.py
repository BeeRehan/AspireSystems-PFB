from django.urls import path
from . import views

urlpatterns = [
    path('reject/<int:pk>',views.reject, name='reject'),
    path('approve/<int:pk>',views.approve, name='approve'),
]
