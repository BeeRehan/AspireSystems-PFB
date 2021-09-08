from django.urls import path
from . import views

urlpatterns = [
    path('',views.to_login,name='Loginpage'),
    path('logout',views.logout,name='logout'),
    path('password_reseter',views.password_reseter,name="password_reseter"),
    path('password_reset',views.password_reset,name="password_reset"),
    path('authenticate_user',views.authenticate_user,name='authenticate_user'),
    path('go_admin_page',views.go_admin_page,name='go_admin_page'),
    path('create_user',views.create_user,name='create_user'),
    path('to_create_user',views.to_create_user,name='to_create_user'),   
    path('to_delete_user/<int:pk>',views.to_delete_user,name='to_delete_user'),   
    path('show_user_profile',views.show_user_profile,name='show_user_profile'),  
    path('reset_user_profile',views.reset_user_profile,name='reset_user_profile'), 
    path('show_forgot_password_form',views.show_forgot_password_form,name='show_forgot_password_form'),   
    path('to_reset_password',views.to_reset_password,name='to_reset_password'), 
]
