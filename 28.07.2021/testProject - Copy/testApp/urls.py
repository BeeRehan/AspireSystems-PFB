from django.urls import path
from . import views

urlpatterns = [
    path('insert', views.insert, name='insert'),
    path('show', views.show, name='show'),
    path('add_product', views.add_product, name='add_product'),
    path('get', views.get, name='get'),
    path('post', views.post, name='post'),
]