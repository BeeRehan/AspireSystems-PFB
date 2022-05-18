from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=25)
    price = models.IntegerField()
    category = models.CharField(max_length=10)
    image_url = models.URLField()
    quantity = models.IntegerField(default=1)

class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    mobile_number = PhoneNumberField()