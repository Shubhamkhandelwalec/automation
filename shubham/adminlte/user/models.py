from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    mobile = models.BigIntegerField()
    dob = models.DateTimeField()
    image = models.FileField(upload_to='media/')
    uniqueid = models.IntegerField(max_length=200)
    sub_title = models.CharField(max_length=150)
    status = models.BooleanField(default=False)
    ismobile = models.BooleanField(default=False)
    isemail = models.BooleanField(default=False)
    REQUIRED_FIELDS = ['mobile','dob','image','sub_title','status','ismobile','isemail']


