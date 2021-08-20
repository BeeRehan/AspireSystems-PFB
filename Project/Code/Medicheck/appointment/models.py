from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import SET_DEFAULT
# Create your models here.
class AppoinmentDetails(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField()
    doctor = models.CharField(max_length=20)
    status = models.CharField(max_length=20)