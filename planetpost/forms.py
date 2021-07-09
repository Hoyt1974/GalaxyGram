from django import forms
from .models import *
  
class PlanetPostForm(forms.ModelForm):
  
    class Meta:
        model = Planet_Post
        fields = ['planet_img', 'post']


    #     planet_img = models.ImageField(upload_to='images/')
    # author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    # post = models.CharField(max_length=140)
    # creation_time = models.DateTimeField(default=timezone.now)
    # up_vote = models.IntegerField(default=0)
    # down_vote = models.IntegerField(default=0)
    # total_votes = models.IntegerField(default=0)