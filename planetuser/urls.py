from django.conf.urls import include, url
from rest_framework import routers
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('myuser', UserViewSet)

urlpatterns = [
  url(r"^api/", include(router.urls))
]