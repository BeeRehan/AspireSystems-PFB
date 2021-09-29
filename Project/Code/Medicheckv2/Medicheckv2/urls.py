from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path, include
from django.contrib.auth.models import User, Group

admin.autodiscover()

from rest_framework import generics, permissions, serializers

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# first we define the serializers
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ("name",)


# Create the API views
class UserList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupList(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    required_scopes = ["groups"]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


urlpatterns = [
    path("", views.get_homepage, name="get_homepage"),
    path("admin/", admin.site.urls),
    path("appointment/", include("appointment.urls"), name="appoinment"),
    path("checkup/", include("checkup.urls"), name="checkup"),
    path("users/", include("users.urls"), name="users"),
    path("o/", include("oauth2_provider.urls", namespace="oauth2_provider")),
    path("users/", UserList.as_view()),
    path("users/<pk>/", UserDetails.as_view()),
    path("groups/", GroupList.as_view()),
]
