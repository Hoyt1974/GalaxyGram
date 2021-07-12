from django import forms


class LoginForm(forms.Form):
  username = forms.CharField(max_length=33)
  password = forms.CharField(widget=forms.PasswordInput, max_length=33)