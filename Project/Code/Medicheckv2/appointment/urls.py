from django.urls import path
from . import views

urlpatterns = [
    path("doctor", views.doc_homepage, name="users.index"),
    path("checklist", views.checklist, name="users.checklist"),
    path("approval/<int:pk>", views.approval, name="users.approval"),
    path("appoinment", views.appoinment, name="patient"),
    path("patient", views.pat_homepage, name="users.index"),
    path("apply_appoinment", views.apply_appoinment, name="users.apply_appoinment"),
    path("get_details/<int:pk>/<int:ak>", views.get_details, name="users.get_details"),
    path("reject/<int:pk>", views.reject, name="reject"),
    path("approve/<int:pk>", views.approve, name="approve"),
    path("api/patient", views.api_get_patient, name="users.index"),
    path("api/patientt", views.api_get_patientt, name="api_get_patientt"),
    path("api/doctor", views.api_doc_homepage, name="api_get_patientt"),
    path("api/post_patient", views.api_patient_post_checklist, name="users.index"),
    path("api/apply_appoinment", views.api_apply_appoinment, name="api_apply_appoinment"),
    path("api/approve/<str:pk>", views.api_approve, name="api_approve"),
    path("api/reject/<str:pk>", views.api_reject, name="api_reject"),
    path("api/get_details/<str:pk>/<str:ak>", views.api_get_details, name="api_get_details"),
]
