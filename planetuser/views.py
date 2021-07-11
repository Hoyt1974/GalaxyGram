from django.shortcuts import render
from .models import MyUser


def index_view(request):
  message="hello galaxy"
  return render(request, 'index.html', {'incoming': message})

