from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    age = models.IntegerField()
    reason  = models.CharField(max_length=100)
    gender = models.CharField(max_length=8)
    doctor_name = models.CharField(max_length=20)
    vaccinated  =models.CharField(max_length=7)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')