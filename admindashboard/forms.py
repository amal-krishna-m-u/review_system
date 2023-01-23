from django import forms

class AddUserForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)
    is_admin = forms.BooleanField(required=False)
