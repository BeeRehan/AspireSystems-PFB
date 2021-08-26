from abc import ABCMeta
from django import forms
from django.forms.fields import CharField
from django.forms.widgets import Textarea

class checklistForm(forms.Form):
    #id = forms.IntegerField(label="Appoinment id")
    temprature = forms.CharField(label="Temprature",max_length=10)
    sugar_level = forms.CharField(label="Sugar Level",max_length=10)
    bp_level = forms.CharField(label="BP level",max_length=10)
    advice = forms.CharField(label="Advice",widget=Textarea,max_length=120)
    prescription = forms.CharField(label="Prescription",widget=Textarea,max_length=100)
    con_deseas = forms.CharField(label="Diseases",max_length=100)
