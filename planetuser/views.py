from django.utils import timezone
from django.http.response import HttpResponseRedirect
from django.views import View
from django.views.generic.edit import UpdateView
from django.shortcuts import get_object_or_404, render, redirect, reverse
from .models import MyUser
from planetpost.models import Planet_Post
from .forms import ProfileEditForm
# change to an @login_required decorator instead of if statement????
# throws error if no users in database when trying to access homepage
def index_view(request):
  if request.user.is_authenticated:
    posts=Planet_Post.objects.all()
    return render(request, 'index.html', {'incoming': posts})
  elif MyUser.objects.all():
    return redirect('login')
  else:
    return redirect('signup')


class ProfileView(View):
  class Meta:
    model = MyUser
  
  def get(self, request, user_id):
    my_user=MyUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': my_user})

# class ProfileEditView(UpdateView):
#   template_name='generic_form.html'
#   model=MyUser
#   fields=[
#     'username', 
#     'first_name', 
#     'last_name',
#     'email',
#     'bio'
#     ]
#   def post(self):

#   return render(request, 'profile.html', {'user_id':user_id})
#   def get_object(self):
#     object=get_object_or_404(MyUser, id=self.kwargs['user_id'])
#     return object




def profile_edit(request, user_id):
  my_user=MyUser.objects.get(id=user_id)
  if request.method =='POST' and request.user.id == user_id:
    form=ProfileEditForm(request.POST, instance=my_user)
    if form.is_valid():
      data=form.cleaned_data
      print(data)
      my_user.save()
    else:
      print(my_user.id)
    return HttpResponseRedirect(reverse('home'))
  form=ProfileEditForm(instance=my_user)
  return render(request, 'generic_form.html', {'form': form}) 