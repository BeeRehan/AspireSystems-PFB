from django.contrib import admin
from django.urls import include, path
from testApp import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', views.index,name="index"),
    path('api-auth/', include('rest_framework.urls')),
    path('testApp/', include('testApp.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
