from django.contrib import admin
from .models import *
# Register your models here.


class HomeImageAdminSite(admin.ModelAdmin):
    def home_image_name(self, obj):
        return obj.home_image.name
    list_display = ('id', 'home_image_name', 'created_at')


class SocialMediaUrlLogoIconAdminSite(admin.ModelAdmin):
    list_display = ('id', 'social_media_logo_class', 'social_media_logo_name', 'social_media_logo_url', 'created_at')


admin.site.register(HomeImage, HomeImageAdminSite)
admin.site.register(SocialMediaUrlLogoIcon, SocialMediaUrlLogoIconAdminSite)
