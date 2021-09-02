from users.models import UserProfile
from django import forms
import re
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import ugettext as uge
from . import models
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.shortcuts import render,redirect


def PasswordValidation(value):
        if not len(re.findall('\d', value)) >= 3:
            raise ValidationError(uge('atleast 3 numbers needed!'))
        elif not len(value) > 10:
            raise ValidationError(uge('Minimum password length is 11!'))
        elif not re.findall('[()[\]|\\`~!@#$%^&*_\-+=;:\'",<>./?]', value):
            raise ValidationError(uge('atleast 1 special character needed!'))
        else:
            return True

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",widget=forms.PasswordInput())

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

