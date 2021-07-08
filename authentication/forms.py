from django import forms
from django.db.models.fields import CharField


class LoginForm(forms.Form):
  username = forms.CharField(max_length=33)
  password = forms.CharField(widget=forms.PasswordInput)