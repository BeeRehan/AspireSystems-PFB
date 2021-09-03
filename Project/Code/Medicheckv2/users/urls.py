from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='Loginpage'),
    path('logout',views.logout,name='logout'),
    path('password_reseter',views.password_reseter,name="password_reseter"),
    path('password_reset',views.password_reset,name="password_reset"),
    path('authenticate_user',views.authenticate_user,name='authenticate_user'),
    path('go_admin_page',views.go_admin_page,name='go_admin_page'),
    path('create_user',views.create_user,name='create_user'),
    path('to_create_user',views.to_create_user,name='to_create_user'),   
]
