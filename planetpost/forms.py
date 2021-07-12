from django import forms
from .models import *
  
class PlanetPostForm(forms.ModelForm):
  
    class Meta:
        model = Planet_Post
        fields = ['planet_img', 'post', 'body', 'title']

class UserPostForm(forms.ModelForm):
  
    class Meta:
        model = Planet_Comments
        fields = ['comment']


   