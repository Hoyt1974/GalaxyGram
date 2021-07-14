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
from django.conf.urls import handler400, handler404, handler500
from django.contrib import admin
from django.urls import path

from authentication import views
from authentication.views import SignupView
from planetuser.views import index_view
# from planetmodel.views import planet_view, planet_detail_view
from planetpost.views import planet_post_detail, post_form_view, add_comment, post_list, upvote_view, downvote_view, total_vote, comment_upvote_view, comment_downvote_view, comment_total_vote, comment_edit, post_edit, comment_delete, post_delete
from django.conf import settings
from django.conf.urls.static import static
from planetmodel.views import PlanetDetailView, PlanetView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index_view, name='home'),
    path('signup/', SignupView.as_view()),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view,name= 'logout'),
    path('planet/', PlanetView.as_view(), name='planet'),
    path('planet_post/<int:post_id>/', planet_post_detail, name="post"),
    path('addpost/', post_form_view, name='addpost'),
    path('planet_post/<int:post_id>/add_comment/', add_comment, name='addcomment'),
    path('planet_post/post_list/', post_list, name='postlist'),
    path("up_vote/<int:post_id>/", upvote_view, name="Upvote"),
    path("down_vote/<int:post_id>/", downvote_view, name="Downvote"),
    path('total_vote/', total_vote),
    path('comment_up_vote/<int:comment_id>/', comment_upvote_view, name="CommentUpvote"),
    path('comment_down_vote/<int:comment_id>/', comment_downvote_view, name="CommentDownvote"),
    path('comment_total_vote', comment_total_vote),
    path('comment_edit/<int:comment_id>/', comment_edit, name="CommentEdit"),
    path('post_edit/<int:post_id>/', post_edit, name="PostEdit"),
    path('comment_delete/<int:comment_id>/', comment_delete, name="CommentDelete"),
    path('post_delete/<int:post_id>/', post_delete, name="PostDelete"),

#     path("planet/<int:planet_id>/", planet_detail_view, name="planet_detail"),
    path("planet/<int:planet_id>/", PlanetDetailView.as_view(), name="planet_detail"),
]
# urlpatterns += api_urls
# <int:planet_id>/'


handler404 = 'authentication.views.error_404_view'
handler500 = 'authentication.views.error_500_view'


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)