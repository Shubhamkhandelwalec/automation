from django.db import models
from ckeditor.fields import RichTextField
FAQs_CHOICES = [
    ('Installation', 'Installation'),
    ('Use', 'Use'),
    ('Purchase', 'Purchase'),
    ('Warranty &amp; Return', 'Warranty &amp; Return'),
    ('App', 'App'),
]


# Create your models here.
class AboutSmartPhoneAppTitle(models.Model):
    title_name = models.CharField(max_length=200)
    title_image = models.ImageField(upload_to='App_title_images/',
                                    default='App_title_images/App_title_images_default.png')
    smart_phone_app_description = RichTextField(max_length=5000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AboutSmartPhoneAppImages(models.Model):
    title_id = models.ForeignKey(AboutSmartPhoneAppTitle, on_delete=models.CASCADE)
    app_images = models.ImageField(upload_to='app_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AboutSmartPhoneAppSpecification(models.Model):
    about_smart_phone_app_id = models.ForeignKey(AboutSmartPhoneAppTitle, on_delete=models.CASCADE)
    specification_title = models.CharField(max_length=200)
    specification_logo_class = models.CharField(max_length=200,
                                                help_text='https://mdbootstrap.com/docs/jquery/content/icons-list/')
    specification_description = RichTextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    title_name = models.CharField(max_length=200)
    description = RichTextField(max_length=5000)
    logo_class = models.CharField(max_length=200, help_text='https://mdbootstrap.com/docs/jquery/content/icons-list/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class AboutVideo(models.Model):
    about_video = models.FileField(upload_to='about_video/')
    about_title = models.CharField(max_length=200)
    about_description = RichTextField(max_length=5000)
    about_image = models.ImageField(upload_to='about_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class ConnectivityDevices(models.Model):
    description = RichTextField(max_length=20000)
    image = models.ImageField(upload_to='ConnectivityDevices/')
    url = models.TextField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class HowItWorks(models.Model):
    description = RichTextField(max_length=20000)
    image = models.ImageField(upload_to='HowItWorks/')
    url = models.TextField(max_length=20000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


class FAQs(models.Model):
    faq_question = RichTextField(max_length=1000)
    description = RichTextField(max_length=2000)
    faq_for = models.CharField(max_length=200, choices=FAQs_CHOICES, default='App')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
