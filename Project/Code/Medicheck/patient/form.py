from django.forms.fields import DateField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, RadioSelect
from .models import UserProfile
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as uge

import datetime

# def date_validate(value):
#     print(value)
#     print(datetime.date.today())
#     if(not (value > datetime.date.today())):
#         raise ValidationError(uge('Enter the correct date!!!'))
#     else:
#         return True

class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class PatientDetails(forms.Form):
    name = forms.CharField(label="Patient Name",max_length=20,disabled=True,required=False)
    age = forms.IntegerField(label="Age",disabled=True,required=False)
    date = forms.DateField(widget=DateInput)
    time = forms.TimeField(widget=TimeInput)
    reason = forms.CharField(label="Reason",max_length=100)
    doctor = forms.ChoiceField(label="Doctor",choices=(("mohamed","Mohamed"),("rakesh","Rakesh")))
    scan_report = forms.FileField()
    vaccinated = forms.ChoiceField(label="Covid Vaccinaed",choices=[("yes","Yes"),("no","No")],widget=RadioSelect)
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")),disabled=True,required=False)