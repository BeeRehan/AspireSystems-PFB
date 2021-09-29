from django import forms

class ApprovalForm(forms.Form):
    status = forms.ChoiceField(label="Approval",choices=(("approved","Approve"),("canceled","Cancel")))
