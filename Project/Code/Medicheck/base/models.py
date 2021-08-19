from django.db import models

# Create your models here.
class UserProfile(models.Model):
    age = models.IntegerField()
    gender = models.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")))
    file = models.FileField(upload_to ='uploads/% Y/% m/% d/')
