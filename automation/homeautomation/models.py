from django.db import models

# Create your models here.


class ContactUs(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone_no = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    client_ip = models.CharField(max_length=100, null=True, blank=True)
    client_browser = models.CharField(max_length=200, null=True, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
