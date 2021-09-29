from django.db import models
from appointment.models import AppoinmentDetails

# Create your models here.
class CheckupDetails(models.Model):
    appointment = models.ForeignKey(AppoinmentDetails, on_delete=models.CASCADE)
    temprature = models.CharField(max_length=10)
    sugar_level = models.CharField(max_length=10)
    bp_level = models.CharField(max_length=10)
    Advice = models.CharField(max_length=100)
    prescription = models.CharField(max_length=100)
    confirmed_diseases = models.CharField(max_length=100)
