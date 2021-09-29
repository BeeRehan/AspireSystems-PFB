from django import forms
from .models import Products

class FormProductForm(forms.ModelForm):
    class Meta:
        model= Products
        fields= ["name", "category", "color", "price"]
