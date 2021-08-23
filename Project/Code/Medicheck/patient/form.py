from django.forms.fields import DateField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, RadioSelect
from .models import UserProfile
from django import forms

class PatientDetails(forms.Form):
    name = forms.CharField(label="Patient Name",max_length=20,disabled=True,required=False)
    age = forms.IntegerField(label="Age",disabled=True,required=False)
    date = forms.DateField()
    time = forms.TimeField()
    reason = forms.CharField(label="Reason for appoinment",max_length=100)
    doctor = forms.ChoiceField(label="Doctor",choices=(("mohamed","Mohamed"),("rakesh","Rakesh")))
    scan_report = forms.FileField()
    vaccinated = forms.ChoiceField(label="Covid Vaccinaed",choices=[("yes","Yes"),("no","No")],widget=RadioSelect)
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")),disabled=True,required=False)