from django import forms
import re
from django.core.exceptions import ValidationError
from django.forms import fields
from django.utils.translation import ugettext as uge
from . import models

class UserLoginForm(forms.Form):
    username = forms.CharField(label="Username",max_length=30)
    password = forms.CharField(label="Password",widget=forms.PasswordInput())
