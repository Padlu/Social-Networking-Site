from django.contrib import admin

from .models import Signup, Newsfeed, Comments, Friends
# Register your models here.

admin.site.register(Signup)
admin.site.register(Newsfeed)
admin.site.register(Comments)
admin.site.register(Friends)