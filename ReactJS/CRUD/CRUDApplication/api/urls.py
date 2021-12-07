from django.urls import path
from . import   views

urlpatterns = [
    path('list-urls/', views.list_urls),
    path('rest-list/', views.list_data),
    path('rest-create/', views.insert_data),   
    path('rest-get/<str:pk>/', views.get_data),  
    path('rest-update/<str:pk>/', views.update_data),  
    path('rest-delete/<str:pk>/', views.delete_data),    
]