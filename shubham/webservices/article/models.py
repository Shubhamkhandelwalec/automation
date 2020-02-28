from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Article(models.Model):
    userid = models.ForeignKey(User,on_delete = models.CASCADE,null=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='media/')
