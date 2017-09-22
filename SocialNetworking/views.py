from django.shortcuts import render
import datetime, os
from django.db import models
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django import forms
from .suform import CreateSignUpForm
from django.views.generic import TemplateView,ListView,DetailView
from .models import Signup, Newsfeed, Comments, Friends

# <------------------SignUp AND Login------------------> #



user = Signup.objects.latest('lastloggedin')

incorrect_login = False

def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

# Create your views here.

def user_createview(request):
    global user
    if request.method == "POST":
        firstn = request.POST.get("firstname")
        lastn  = request.POST.get("lastname")
        email_id = request.POST.get("email_id")
        password = request.POST.get("password")
        user = Signup.objects.create(
            firstn = firstn,
            lastn = lastn,
            email_id = email_id,
            password = password,
            lastloggedin = str(datetime.date.today()) + " " + datetime.datetime.now().strftime('%H:%M:%S'),
        )
        return HttpResponseRedirect("/signup-personal/")
    template_name = 'suform.html'
    context = {}
    return render(request, template_name, context)


def user_suprsnlview(request):
    global user
    print(user)
    if request.method == "POST":
        mobile = request.POST.get("mobile")
        address  = request.POST.get("address")
        birthdate = request.POST.get("birthdate")
        gender = request.POST.get("gender")
        languages = request.POST.get("languages")
        image = request.POST.get("userdisplay")
        # if image == "":
        #     os.remove(user.display.path)
        # user.display.delete(save = False)
        Signup.objects.filter(firstn__exact=user.firstn).update(
            mobile = mobile,
            address = address,
            birthdate = birthdate,
            gender = gender,
            languages = languages,
            display = image,
        )
        print(user.display)
        user.save()
        return HttpResponseRedirect("/newsfeed-user/")
    template_name = 'personal.html'
    context = {}
    return render(request, template_name, context)

def login():
    global incorrect_login
    if incorrect_login == True:
        incorrect_login= False
        return True
    else:
        return False

def user_loginview(request):
    global incorrect_login
    if request.method == "POST":
        email_id = request.POST.get("email_id")
        password = request.POST.get("password")
        object = Signup.objects.values()
        length = len(object)
        for i in range(length):
            if email_id == object[i]["email_id"] and password == object[i]["password"]:
                global user
                print(user)
                user = Signup.objects.get(email_id__exact=email_id)
                print(user)
                return HttpResponseRedirect("/newsfeed-user/")
        incorrect_login = True
        return HttpResponseRedirect("/login/")
    template_name = 'login.html'
    if login():
        context = {
            'incorrect' : True
        }
    else:
        context = {
            'incorrect' : False
        }
    return render(request, template_name, context)


# <------------------Newsfeed AND Posts AND Comments------------------> #


thispost = None

currentpost = None

thiscomment = None

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
    global thispost
    global user
    print(user)
    if request.method == "POST":
        post = request.POST.get("post")
        postmodified = post
        postmodified.replace(" ","")
        image = request.FILES.get("filereq")
        thispost = Newsfeed.objects.create(
            containern = user,
            post = post,
            postmodified = postmodified,
            datepubchar = str(datetime.date.today()) + "-" + datetime.datetime.now().strftime('%H-%M-%S'),
            datepublished = datetime.date.today(),
            image = image,
        )
        thispost.save()
        pos = True
        return HttpResponseRedirect("/newsfeed-user/")
    template_name = 'usernf.html'
    if postit():
        context = {
            'user' : user, 'post' : thispost, 'posted' : True, 'Users' : Signup.objects.all()
        }
    else:
        context = {
            'user': user, 'post' : thispost, 'posted' : False, 'Users' : Signup.objects.all()
        }

    return render(request, template_name, context)

def comment(request, post):
    global thiscomment
    global thispost
    global currentpost
    global user
    print(user)
    print(post)
    thispost = Newsfeed.objects.get(datepubchar__exact=post)
    user.save()
    print(thispost)
    if request.method == "POST":
        comment = request.POST.get("comment")
        thiscomment = Comments.objects.create(
            containerc = thispost,
            comment = comment,
            datecomchar = str(datetime.date.today()) + "-" + datetime.datetime.now().strftime('%H-%M-%S'),
            datecommented = datetime.date.today(),
            user = str(user.email_id),
        )
        thiscomment.save()
        return HttpResponseRedirect("/newsfeed-user/")
    template_name = 'usernf.html'
    context = {
            'user': user, 'post' : thispost, 'posted' : False, 'Users' : Signup.objects.all()
    }

    return render(request, template_name, context)


# <------------------FriendRequests------------------> #

def request(request, fuser):
    global user
    global thispost
    if request.method == "GET":
        frienduser = Signup.objects.get(firstn__exact=fuser)
        print(frienduser.friends_set.all())
        if frienduser.friends_set.filter(super__email_id__exact=user.email_id) is None :
            obj = Friends.objects.create(
                super = frienduser,
                friend_name = str(user.email_id),
            )
            frienduser.followers = F('followers') + 1
            frienduser.save()
    template_name = 'usernf.html'
    context = {
        'user' : user, 'post' : thispost, 'posted' : False, 'Users' : Signup.objects.all()
   }
    return render(request, template_name, context)

# <------------------Likes AND Dislikes------------------> #

def likeit(request, post):
    global user
    global thispost
    if request.method == "GET":
        likedpost = Newsfeed.objects.get(datepubchar__exact=post)
        likedpost.likes = F('likes') + 1
        likedpost.save()
    template_name = 'usernf.html'
    context = {
        'user': user, 'post': thispost, 'posted': False, 'Users': Signup.objects.all()
    }
    return render(request, template_name, context)

def dislikeit(request, post):
    global user
    global thispost
    if request.method == "GET":
        dislikedpost = Newsfeed.objects.get(datepubchar__exact=post)
        dislikedpost.dislikes = F('dislikes') + 1
        dislikedpost.save()
    template_name = 'usernf.html'
    context = {
        'user': user, 'post': thispost, 'posted': False, 'Users': Signup.objects.all()
    }
    return render(request, template_name, context)