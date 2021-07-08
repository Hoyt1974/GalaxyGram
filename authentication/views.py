from django.shortcuts import render, reverse, redirect
from django.http.response import HttpResponseRedirect
from django.contrib.auth import authenticate, login,logout
from authentication.forms import LoginForm

# Create your views here.

def login_view(request):
  if request.method == "POST":
    form = LoginForm(request.POST)
    if form.is_valid():
      data=form.cleaned_data
      log=authenticate(
        request,
        username=data.get('username'),
        password=data.get('password')
      )
      if log:
        login(request, log)
        # log.save()
        return HttpResponseRedirect(request.GET.get("next", "/"))

  form = LoginForm()
  return render(request, 'generic_form.html', {'form': form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

def index_view(request):
  if request.user.is_authenticated:
    placeholder = "Placeholder.objects.order_by('post_created')"
    return render(request, 'index.html', {'incoming': placeholder})
  return HttpResponseRedirect(reverse('login'))
