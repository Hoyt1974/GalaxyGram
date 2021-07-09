from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect


def index_view(request):
  message="hello galaxy"
  return render(request, 'index.html', {'incoming': message})

