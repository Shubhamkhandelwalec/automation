from django.db import models


class Registration(models.Model):
    user_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=150)
    # confirm_password = models.CharField(max_length=30)
    token = models.CharField(max_length=200)
    isverified = models.BooleanField(default=False)
    profile_img = models.ImageField(upload_to= 'media/')
    randomid = models.IntegerField(max_length=50,default=0, unique=True)

class TempRegister(models.Model):
    username = models.CharField(max_length=100)
    fullname = models.CharField(max_length=100)
    gmail = models.EmailField(max_length=100)
    randomid = models.IntegerField(max_length=50,unique=True)
    currentdate = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)


