"""planetgram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from authentication import views
from planetuser.views import index_view
from planetmodel.views import planet_view
from planetpost.views import planet_post_detail, post_form_view, add_comment#, planet_comments_list
# from planetuser import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view),
    path('planet/', planet_view, name='planet'),
    path('planet_post/<int:post_id>/', planet_post_detail, name="post"),
    path('addpost/', post_form_view, name='addpost'),
    path('planet_post/<int:post_id>/add_comment/', add_comment, name='addcomment'),
    # path('comment/', planet_comments_list, name='comment'), change to add comment view

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)