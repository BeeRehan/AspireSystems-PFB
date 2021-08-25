from django.forms.fields import DateField
from django.forms.widgets import DateInput, DateTimeBaseInput, DateTimeInput, RadioSelect
from .models import UserProfile
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as uge

import datetime

def date_validate(value):
    print("Validator",value)
    print(datetime.date.today())
    if(not (value > datetime.date.today())):
        raise ValidationError(uge('Enter the correct date!!!'))
    else:
        return True

def time_validate(value):
    print("Validator",value)
    print(datetime.datetime.now().strftime("%H:%M:%S"))
    h,m,s = str(value).split(':')
    now = datetime.datetime.now()
    value = now.replace(hour=int(h),minute=int(m),second=int(s),microsecond=0)
    h,m,s = datetime.datetime.now().strftime("%H:%M:%S").split(':')
    now = now.replace(hour=int(h),minute=int(m),second=int(s),microsecond=0)
    print(type(value),type(now))
    if(not (value >now)):
        raise ValidationError(uge('Enter the correct time!!!'))
    else:
        return True


class DateInput(forms.DateInput):
    input_type = 'date'

class TimeInput(forms.TimeInput):
    input_type = 'time'

class PatientDetails(forms.Form):
    name = forms.CharField(label="Patient Name",max_length=20,disabled=True,required=False)
    age = forms.IntegerField(label="Age",disabled=True,required=False)
    date = forms.DateField(widget=DateInput,validators=[date_validate])
    time = forms.TimeField(widget=TimeInput,validators=[time_validate])
    reason = forms.CharField(label="Reason",max_length=100)
    doctor = forms.ChoiceField(label="Doctor",choices=(("mohamed","Mohamed"),("rakesh","Rakesh")))
    scan_report = forms.FileField()
    vaccinated = forms.ChoiceField(label="Covid Vaccinaed",choices=[("yes","Yes"),("no","No")],widget=RadioSelect)
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")),disabled=True,required=False)