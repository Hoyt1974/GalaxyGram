from django import forms
from .models import *

class ProfileEditForm(forms.ModelForm):
  class Meta:
    model = MyUser
    fields = ['username', 'first_name', 'last_name', 'email', 'bio']