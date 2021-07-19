from django import forms
from .models import *
  
class PlanetPostForm(forms.ModelForm):
  
    class Meta:
        model = Planet_Post
        fields = ['planet_img', 'title', 'post']

class UserPostForm(forms.ModelForm):
  
    class Meta:
        model = Planet_Comments
        fields = ['comment']
