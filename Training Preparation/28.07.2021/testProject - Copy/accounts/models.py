from django.db import models
from django.contrib.auth.models import User, auth
# Create your models here.

class UserInfo(models.Model):
    gender = models.CharField(max_length=20)
    dob = models.DateField()
    bio = models.TextField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
