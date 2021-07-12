from django.shortcuts import render
from .models import MyUser
from planetpost.models import Planet_Post

# change to an @login_required decorator instead of if statement????
# throws error if no users in database when trying to access homepage
def index_view(request):
  if request.user.is_authenticated:
    posts=Planet_Post.objects.all()
  return render(request, 'index.html', {'incoming': posts})

def profile_view(request, user_id):
  my_user= MyUser.object.get(id=user_id)
  