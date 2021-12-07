from django import forms
from django.forms.widgets import Textarea
import re
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as uge

def PasswordValidation(value):
        if not len(re.findall('\d', value)) >= 3:
            raise ValidationError(uge('atleast 3 numbers needed!'))
        elif not len(value) > 10:
            raise ValidationError(uge('Minimum password length is 11!'))
        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(uge('atleast 1 special character needed!'))
        else:
            return True

class UserRegistrationForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    email = forms.EmailField(label='Email')
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label="Password",widget=forms.PasswordInput(),validators=[PasswordValidation])
    password1 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput())
    gender = forms.ChoiceField(label="Gender",choices=(("male","Male"),("female","Female")))
    #admincheck = forms.ChoiceField(label="Admin User",widget=forms.CheckboxInput())
    dob = forms.DateField(label="Date of Birth")
    bio = forms.CharField(label="Bio",widget=Textarea(),required=False)

class UserLoginForm(forms.Form):
    username = forms.CharField(label='Username',max_length=20)
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
