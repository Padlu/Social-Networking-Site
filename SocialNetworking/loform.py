from django import forms

class CreateLoginForm(forms.Form):
    email_id   = forms.CharField(required=False)
    password   = forms.CharField(required=False)