from django import forms  
from .models import Products
'''
class ProductForm(forms.Form):  
    name = forms.CharField(label="Enter The Name ",max_length=50)  
    category  = forms.CharField(label="Enter the Category ", max_length = 100)
    color = forms.CharField(label="Enter The Color", max_length = 100)
    price = forms.CharField(label="Enter The Price ", max_length = 100)
    
'''
class FormProductForm(forms.ModelForm):
    class Meta:
        model= Products
        fields= ["name", "category", "color", "price"]