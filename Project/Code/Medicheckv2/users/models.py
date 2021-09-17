from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=8)
    secret_key = models.CharField(max_length=15, default="")
    attempt = models.IntegerField(default=0)
    account_status = models.CharField(max_length=20, default="Open")
    image = models.ImageField(default="default.png", upload_to="profile_pics")
