from django.db import models


class HomeImage(models.Model):
    home_image = models.ImageField(upload_to='home/', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class SocialMediaUrlLogoIcon(models.Model):
    social_media_logo_class = models.CharField(max_length=250)
    social_media_logo_name = models.CharField(max_length=250)
    social_media_logo_url = models.TextField(max_length=2500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)



