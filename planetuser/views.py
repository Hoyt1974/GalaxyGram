from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .serializers import UserSerializer
from .models import MyUser

# Create your views here.

class UserViewSet(ModelViewSet):
  serializer_class = UserSerializer
  queryset = MyUser.objects.all()