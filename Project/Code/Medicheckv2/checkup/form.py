from django import forms
from django.forms.widgets import Textarea
from .models import CheckupDetails
from appointment.models import AppoinmentDetails


class checklistForm(forms.Form):
    # id = forms.IntegerField(label="Appoinment id")
    temprature = forms.CharField(label="Temprature", max_length=10)
    sugar_level = forms.CharField(label="Sugar Level", max_length=10)
    bp_level = forms.CharField(label="BP level", max_length=10)
    advice = forms.CharField(label="Advice", widget=Textarea, max_length=120)
    prescription = forms.CharField(
        label="Prescription", widget=Textarea, max_length=100
    )
    con_deseas = forms.CharField(label="Diseases", max_length=100)

    def save(self, pk):
        app = AppoinmentDetails.objects.get(id=pk)
        app.status = "checked"
        app.save()
        check = CheckupDetails.objects.create(
            temprature=self.cleaned_data["temprature"],
            sugar_level=self.cleaned_data["sugar_level"],
            bp_level=self.cleaned_data["bp_level"],
            Advice=self.cleaned_data["advice"],
            prescription=self.cleaned_data["prescription"],
            confirmed_diseases=self.cleaned_data["con_deseas"],
            appointment_id=pk,
        )
        check.save()
