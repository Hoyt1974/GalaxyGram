from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer
from .models import MyUser

# Create your views here.

class UserViewSet(ModelViewSet):
  serializer_class = UserSerializer
  queryset = MyUser.objects.all()
from django.http.response import HttpResponse, HttpResponseRedirect


def index_view(request):
  message="hello galaxy"
  return render(request, 'index.html', {'incoming': message})

