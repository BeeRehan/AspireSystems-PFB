from django.db import models
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=25)
    age = models.IntegerField()
    occupation = models.CharField(max_length=25)


@receiver(pre_save,sender=UserProfile)
def before_save(sender,instance,**kwargs):
    print("Before Save: ",instance)

@receiver(post_save,sender=UserProfile)
def after_save(sender,instance,**kwargs):
    print("User added!!!")