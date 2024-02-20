from django import forms
from django.contrib.auth.forms import AuthenticationForm


class LoginuserForm(AuthenticationForm):
    username = forms.CharField(label='Login')
    password = forms.CharField()