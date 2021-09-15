from django.forms.widgets import DateInput, RadioSelect
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as uge
from appointment.models import AppoinmentDetails
from django.contrib.auth.models import User,Group
from .models import UserProfile
import re
from django.contrib.auth.hashers import make_password
import datetime

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",widget=forms.PasswordInput())

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
    # print(type(value),type(now))
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

    def save(self,request):
            date = self.cleaned_data['date']
            time = self.cleaned_data['time']
            reason = self.cleaned_data['reason']
            doctor = self.cleaned_data['doctor']
            vaccinated = self.cleaned_data['vaccinated']
            file = self.cleaned_data['scan_report'] 
            app = AppoinmentDetails(date=(str(date)+" "+str(time)),vaccinated=vaccinated,file=file,doctor=doctor,
            reason=reason,status="requested",user_id=request.user.id)
            app.save()
        
def PasswordValidation(value):
        if not len(re.findall('\d', value)) >= 3:
            raise ValidationError(uge('atleast 3 numbers needed!'))
        elif not len(value) > 10:
            raise ValidationError(uge('Minimum password length is 11!'))
        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(uge('atleast 1 special character needed!'))
        else:
            return True

class PasswordResetForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    key = forms.CharField(label="Secret Key",max_length=20)
    new_password = forms.CharField(label="New Password",widget=forms.PasswordInput(),validators=[PasswordValidation])
    con_password = forms.CharField(label="Confirm Password",widget=forms.PasswordInput())

    def save(self,user):
        new_password = self.cleaned_data['new_password']
        user = User.objects.get(id=user)
        user_profile = UserProfile.objects.get(user_id=user.id)
        user_profile.attept = 0
        user_profile.account_status  = 'Open'
        user.password = make_password(new_password)
        user_profile.save()
        user.save()
        print("Success!!!")

class CreateUsersForm(forms.Form):
    sname = forms.CharField(label="Username",max_length=15)
    new_password = forms.CharField(label="Password",widget=forms.PasswordInput())
    group = forms.ChoiceField(label="Group",choices=(("patients","Patients"),("doctors","Doctors"),("admins","Admin")))
    age = forms.IntegerField(label="Age")
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")))
    secret_key = forms.CharField(label="Secret Key",max_length=10)

    def save(self):
        name = self.cleaned_data['sname']
        new_password = self.cleaned_data['new_password']
        group = self.cleaned_data['group']
        age = self.cleaned_data['age']
        gender = self.cleaned_data['gender']
        secret_key = self.cleaned_data['secret_key']
        user = User.objects.create_user(username=name,password=new_password)
        user_profile = UserProfile.objects.create(user_id=user.id,age=age,gender=gender,attempt=0,account_status='Open',secret_key=secret_key)
        user_profile.save()
        groups = Group.objects.get(name=group)
        groups.user_set.add(user)
        # user.groups.add(group)
        groups.save()
        user.save()


class ForgotPasswordForm(forms.Form):
    newpwd =  forms.CharField(label="New Password",widget=forms.PasswordInput(),validators=[PasswordValidation])
    repwd =  forms.CharField(label="Re-enter Password",widget=forms.PasswordInput())