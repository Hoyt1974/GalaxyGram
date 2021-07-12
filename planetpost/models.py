from django.db import models
from planetuser.models import MyUser
from django.utils import timezone

class Planet_Post(models.Model):
    title = models.CharField(max_length=200)
    planet_name = models.CharField(max_length=200)
    planet_img = models.ImageField(upload_to='images/')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.CharField(max_length=140)
    creation_time = models.DateTimeField(default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)


class Planet_Comments(models.Model):
    comment = models.CharField(max_length=140)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Planet_Post, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(default=timezone.now)
    up_vote = models.IntegerField(default=0)
    down_vote = models.IntegerField(default=0)
    total_votes = models.IntegerField(default=0)