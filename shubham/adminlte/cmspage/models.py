from django.db import models

# Create your models here.
class Cmspages(models.Model):
    username = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=150)
    meta_keyword = models.CharField(max_length=30)
    slug = models.CharField(max_length=200)
    meta_description = models.CharField(max_length=300)
    short_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/')
    description = models.CharField(max_length=300)
    uniqueid = models.IntegerField(max_length=50, default=0, unique=True)