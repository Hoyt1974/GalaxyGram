from django.db import models
from django.utils import timezone
from planetuser.models import MyUser
from planetmodel.models import Body

class Planet_Post(models.Model):
    body = models.ForeignKey(Body, on_delete=models.CASCADE, related_name="posts")
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