from django.contrib import admin
from django.urls import include, path
from testApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('testApp/', include('testApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
    path('index/', views.index),  
    path('show/',views.show),
    path('ProductList/',views.ProductList.as_view()),
]