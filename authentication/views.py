from planetuser.models import MyUser
from django.shortcuts import render, reverse, redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from authentication.forms import LoginForm
from planetpost.models import Planet_Post
from django.views import View
# Create your views here.


def error_404_view(request, exception):
  return render(request, '404.html')



def error_500_view(request, *args, **kwargs):
  return render(request, '500.html')



class SignupView(View):

  def get(self, request):
    form=LoginForm()
    return render(request, 'generic_form.html', {'form':form })


  def post(self, request):
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      if MyUser.objects.filter(username=data['username']):
        return HttpResponseRedirect(reverse('login'))
      newbie = MyUser.objects.create_user(
        username=data['username'],
        password=data['password']
    )
    newbie.save()
    login(request, newbie)
    return HttpResponseRedirect(reverse('home'))




def login_view(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      data = form.cleaned_data
      user = authenticate(
        request,
        username=data['username'],
        password=data['password']
      )
      if user:
        login(request, user)
        user.save()
        return HttpResponseRedirect(request.GET.get("next", "/"))
  form = LoginForm()
  return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def index_view(request):
    if request.user.is_authenticated:
        posts = Planet_Post.objects.all()
        return render(request, 'index.html', {'incoming': posts})
    return HttpResponseRedirect(reverse('login'))
