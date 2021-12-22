from django.urls import path
from . import views

urlpatterns = [
    path("", views.to_login, name="Loginpage"),
    path("logout", views.logout, name="logout"),
    path("password_reseter", views.password_reseter, name="password_reseter"),
    path("password_reset", views.password_reset, name="password_reset"),
    path("authenticate_user", views.authenticate_user, name="authenticate_user"),
    path("admin", views.go_admin_page, name="go_admin_page"),
    path("create_user", views.create_user, name="create_user"),
    path("to_create_user", views.to_create_user, name="to_create_user"),
    path("to_delete_user/<int:pk>", views.to_delete_user, name="to_delete_user"),
    path("show_user_profile", views.show_user_profile, name="show_user_profile"),
    path("reset_user_profile", views.reset_user_profile, name="reset_user_profile"),
    path(
        "show_forgot_password_form",
        views.show_forgot_password_form,
        name="show_forgot_password_form",
    ),
    path("to_reset_password", views.to_reset_password, name="to_reset_password"),
    path(
        "api/show_user_profile", views.api_show_user_profile, name="show_user_profile"
    ),
    path("api/show_user", views.api_show_user, name="api_show_user"),
    path("api/post_user", views.api_post_user, name="api_post_user"),
    path("api/api_register", views.api_register, name="api_register"),
    path("api/api_get_user_profile", views.api_get_user_profile, name="api_get_user_profile"),
    path("api/api_login", views.api_login, name="api_login"),
    path("api/api_logout", views.api_logout, name="api_logout"),
    path("api/post_user_profile", views.api_post_user_profile, name="api_post_user_profile"),
    path("api/list_users", views.list_data, name="list_data"),
    path("api/add_user", views.api_add_user, name="api_add_user"),
    path("api/delete_data/<str:pk>",views.api_delete_data, name="api_delete_data"),
]
