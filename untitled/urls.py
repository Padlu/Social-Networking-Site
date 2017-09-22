"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import  TemplateView

from SocialNetworking.views import (
    user_createview,
    user_loginview,
    user_suprsnlview,
    post,
    comment,
    request,
    likeit,
    dislikeit,
)

# from Newsfeed.views import (
#     post,
#     comment,
# )

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^signup/$', user_createview),
    url(r'^signup-personal/$', user_suprsnlview, name="signup"),
    url(r'^login/$', user_loginview, name="login"),
    url(r'^newsfeed-user/$', post, name= "post"),
    url(r'^newsfeed-comment/(?P<post>[-\w]+)/$', comment, name="comment"),
    url(r'^newsfeed-req/(?P<fuser>\w+)/$', request, name="request"),
    url(r'^newsfeed-like/(?P<post>[-\w]+)/$', likeit, name="liked"),
    url(r'^newsfeed-dislike/(?P<post>[-\w]+)/$', dislikeit, name="disliked"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)