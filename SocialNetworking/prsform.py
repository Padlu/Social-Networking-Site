from django import forms

class CreatePersonalFrom(forms.Form):
    mobile    = forms.CharField(required=False)
    address   = forms.CharField(required=False)
    birthdate = forms.DateField(required=False)
    gender    = forms.CharField(required=False)
    languages = forms.CharField(required=False)