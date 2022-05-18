from django import views
from django.urls import path
from .views import ApiClass,SignInView,SignupView
urlpatterns = [
    path('products',ApiClass.as_view(),name="Api Class"),
    path('signin',SignInView.as_view(),name="Signin Class"),
    path('signup',SignupView.as_view(),name="SiginUP Class"),
]
