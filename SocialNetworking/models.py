from django.db import models
from django.utils import timezone

# Create your models here.

def image_upload_user(instance, filename):
    return "user_profile" + "/%s/%s" %(instance ,filename)

class Signup (models.Model):
    firstn       = models.CharField(max_length = 50, default="")
    lastn        = models.CharField(max_length = 50, default="")
    email_id     = models.EmailField(max_length = 50, default="")
    password     = models.CharField(max_length = 10, null=False, default="")
    mobile       = models.CharField(max_length = 10, default="")
    address      = models.CharField(max_length = 50, default="")
    birthdate    = models.DateField(auto_now_add=False, default=timezone.now().date())
    gender       = models.CharField(max_length = 50, default="")
    languages    = models.CharField(max_length = 50, default="")
    display      = models.ImageField(upload_to= image_upload_user, blank=True, default="/user_profile/images.png")
    lastloggedin = models.DateTimeField(auto_now=False)
    followers    = models.IntegerField(default=0)

    def __str__(self):
        return self.firstn

    @property
    def title(self):
        return self.firstn

class Friends (models.Model):
    super = models.ForeignKey(Signup, on_delete=models.CASCADE)
    friend_name = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.super)


def image_upload(instance, filename):
    return "posts/" + str(Signup.objects.last().firstn) + "/%s/%s" %(instance.containern_id, filename)

class Newsfeed (models.Model):
    containern    = models.ForeignKey(Signup, on_delete=models.CASCADE, db_index=True)
    post          = models.CharField(max_length=300, default="")
    postmodified  = models.CharField(max_length=300, default="")
    datepubchar   = models.CharField(max_length=20,default="")
    datepublished = models.DateTimeField(auto_now_add=True)
    likes         = models.IntegerField(default=0)
    dislikes      = models.IntegerField(default=0)
    image         = models.ImageField(upload_to=image_upload, verbose_name= image_upload,
                                      null=True, blank=True,
                                      height_field="heightimg",
                                      width_field="widthimg")
    heightimg     = models.IntegerField(default=0)
    widthimg      = models.IntegerField(default=0)

    def __str__(self):
        return str(self.containern) + "-" + str(self.post)

    @property
    def title(self):
        return self.containern

class Comments (models.Model):
    containerc    = models.ForeignKey(Newsfeed, on_delete=models.CASCADE, db_index=True)
    comment       = models.CharField(max_length=300, default="")
    datecomchar   = models.CharField(max_length=20,default="")
    datecommented = models.DateTimeField(auto_now_add=True)
    user          = models.CharField(max_length=50 ,default="")

    def __str__(self):
        return str(self.containerc) + "-" + str(self.comment)