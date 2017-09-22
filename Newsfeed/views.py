from django.shortcuts import render, get_object_or_404
import datetime
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django import forms
from django.views.generic import TemplateView,ListView,DetailView
from SocialNetworking.models import Signup, Newsfd, Comment
from SocialNetworking.views import user


global thispost
thispost = Newsfd.objects.create(
    container = user,
)

global thiscomment
thiscomment = Comment.objects.create(
    container = thispost,
)

def getuser():
    return user

def getpost():
    return thispost

global pos
pos = False

def postit():
    global pos
    if pos == True:
        pos = False
        return True
    else:
        return False

def post(request):
    global pos
    print(user)
    if request.method == "POST":
        post = request.POST.get("post")
        image = request.FILES.get("filereq")
        # thispost.container = user
        # thispost.container_id = 1
        thispost.post = post
        thispost.datepublished = datetime.date.today()
        thispost.image = image
        thispost.save()
        pos = True
        return HttpResponseRedirect("/newsfeed-user/")
    template_name = 'usernf.html'
    if postit():
        context = {
            'user' : getuser(), 'post' : getpost(), 'posted' : True
        }
    else:
        context = {
            'user': getuser(), 'post' : getpost(), 'posted' : False
        }

    return render(request, template_name, context)

def comment(request):

    if request.method == "POST":
        comment = request.POST.get("comment")
        # thiscomment.container = thispost
        # thiscomment.container_id = 1
        thiscomment.comment = comment
        thiscomment.datecommented = datetime.date.today()
        thiscomment.user = user.email_id
        return HttpResponseRedirect("/newsfeed-comment/")
    template_name = 'usernf.html'
    context = {
            'user': getuser(), 'post' : getpost(), 'posted' : False
    }

    return render(request, template_name, context)