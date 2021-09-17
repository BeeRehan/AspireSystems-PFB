from django.urls import path
from . import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('authenticate_user', views.authenticate_user, name='authenticate_user'),
    path('add_user', views.add_user, name='add_user'),
]
