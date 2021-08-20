from django.urls import path
from . import views

urlpatterns = [
    path('authenticate_user',views.authenticate_user, name='authenticate_user'),
    path('logout',views.logout, name='logout'),
]