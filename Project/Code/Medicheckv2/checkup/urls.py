from django.urls import path
from . import views

urlpatterns = [
    path("create_checklist", views.create_checklist, name="checklist.create_checklist"),
    path("add_checklist/<int:pk>", views.add_checklist, name="checklist.add_checklist"),
    path(
        "view_checklist/<int:pk>", views.view_checklist, name="checklist.view_checklist"
    ),
    path(
        "pat_get_checklis/<int:pk>",
        views.pat_get_checklis,
        name="checklist.pat_get_checklis",
    ),
    path(
        "doc_get_checklis/<int:pk>",
        views.doc_get_checklis,
        name="checklist.doc_get_checklis",
    ),
    path(
        "pat_get_checklis/<int:pk>",
        views.pat_get_checklis,
        name="checklist.pat_get_checklis",
    ),
    path(
        "api/pat_get_checklist/<int:pk>",
        views.api_patient_get_checklist,
        name="checklist.pat_get_checklis",
    ),
    path(
        "api/pat_post_checklist/",
        views.api_patient_post_checklist,
        name="checklist.pat_post_checklis",
    ),
    path(
        "api/pat_post_checklist/",
        views.api_patient_post_checklist,
        name="checklist.pat_post_checklis",
    ),
    path(
        "api/post_checklist/<str:pk>",
        views.api_add_checklist,
        name="api.pat_post_checklis",
    ),
    path(
        "api/prev_checklist/<str:pk>",
        views.api_doc_get_checklis,
        name="api_doc_get_checklis",
    ),
    path(
        "api/get_checklist/<str:pk>",
        views.api_get_checklist,
        name="api_get_checklist",
    ),
        path(
        "api/create_checklist",
        views.api_create_checklist,
        name="api_create_checklist",
    ),
]
