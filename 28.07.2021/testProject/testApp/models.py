from django.db import models
from django.db.models.fields import IntegerField

class Products(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    price = models.IntegerField()