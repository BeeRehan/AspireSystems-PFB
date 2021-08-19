from django.forms.widgets import RadioSelect
from .models import UserProfile
from django import forms

class PatientDetails(forms.Form):
    name = forms.CharField(label="Patient Name",max_length=20)
    age = forms.IntegerField(label="Age")
    date = forms.DateTimeField()
    reason = forms.CharField(label="Reason for appoinment",max_length=100)
    doctor = forms.ChoiceField(label="Doctor",choices=(("mohamed","Mohamed"),("kamali","kamali")))
    scan_report = forms.FileField()#upload_to ='uploads/% Y/% m/% d/'
    vaccinated = forms.ChoiceField(label="Doctor",choices=[("yes","Yes"),("no","No")],widget=RadioSelect)
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")))