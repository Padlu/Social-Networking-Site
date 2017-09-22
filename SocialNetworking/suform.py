from django import forms

class CreateSignUpForm(forms.Form):
    firstn     = forms.CharField(required=False)
    lastn      = forms.CharField(required=False)
    email_id   = forms.CharField(required=False)
    password   = forms.CharField(required=False)

    # def clean_name(self):
    #     name = self.cleaned_data.get("name")
    #     if name == "Hello":
    #         raise forms.ValidationError("Not a valid name")
    #     return name