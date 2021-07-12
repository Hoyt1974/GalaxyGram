from django.shortcuts import render
from .models import MyUser
from planetpost.models import Planet_Post

def index_view(request):
  if request.user.is_authenticated:
    posts=Planet_Post.objects.all()
  return render(request, 'index.html', {'incoming':posts})

def profile_view(request, user_id):
  my_user= MyUser.object.get(id=user_id)
  