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

