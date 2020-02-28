from django.db import models
from django.contrib.auth.models import AbstractUser
import json


class User(AbstractUser):
    mobile = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateTimeField()
    is_mobile = models.BooleanField(default=False)
    is_email = models.BooleanField(default=False)
    admin_profile_img = models.ImageField(upload_to="media/")
    updated_at = models.DateTimeField(auto_now=True)
    REQUIRED_FIELDS = ['email', 'mobile', 'date_of_birth', 'is_mobile', 'is_email', 'admin_profile_img', 'updated_at']

