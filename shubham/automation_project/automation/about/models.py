from django.db import models


# Create your models here.
class AboutSmartPhoneAppTitle(models.Model):
    title_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AboutSmartPhoneApp(models.Model):
    title_id = models.ForeignKey(AboutSmartPhoneAppTitle, on_delete=models.CASCADE)
    title_image = models.ImageField(upload_to='App_title_images/')
    app_description = models.TextField(max_length=5000)
    app_images = models.ImageField(upload_to='app_images/')
    specification_title = models.CharField(max_length=200)
    specification_logo_class = models.CharField(max_length=200,
                                                help_text='https://mdbootstrap.com/docs/jquery/content/icons-list/')
    specification_description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title_name = models.CharField(max_length=200)
    description = models.TextField(max_length=5000)
    logo_class = models.CharField(max_length=200, help_text='https://mdbootstrap.com/docs/jquery/content/icons-list/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AboutVideo(models.Model):
    about_video = models.FileField(upload_to='about_video/')
    about_title = models.CharField(max_length=200)
    about_description = models.TextField(max_length=5000)
    about_image = models.ImageField(upload_to='about_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ConnectivityDevices(models.Model):
    pass

