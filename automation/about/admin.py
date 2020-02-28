from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.


class AboutSmartPhoneAppTitleAdminSite(admin.ModelAdmin):
    list_display = ('id', 'title_name', 'created_at')


class AboutSmartPhoneAppAdminSite(admin.ModelAdmin):
    def title_name(self, obj):
        return obj.title_name

    def title_image_name(self, obj):
        return obj.app_images.name
    list_display = ('id', 'title_image_name', 'created_at')
    form = AboutSmartPhoneAppForm


class AboutSmartPhoneAppSpecificationAdminSite(admin.ModelAdmin):
    def title_name(self, obj):
        return obj.title_name

    list_display = ('id', 'title_name', 'specification_title', 'specification_logo_class', 'created_at')
    form = AboutSmartPhoneAppSpecificationForm


class AboutAdminSite(admin.ModelAdmin):
    list_display = ('id', 'title_name', 'created_at')


class AboutVideoAdminSite(admin.ModelAdmin):
    list_display = ('id', 'about_title', 'created_at')


class ConnectivityDevicesAdminSite(admin.ModelAdmin):
    list_display = ('id', 'created_at')


class HowItWorksAdminSite(admin.ModelAdmin):
    list_display = ('id', 'created_at')


class FAQsAdminSite(admin.ModelAdmin):
    list_display = ('id', 'faq_question', 'faq_for', 'created_at')


admin.site.register(AboutSmartPhoneAppTitle, AboutSmartPhoneAppTitleAdminSite)
admin.site.register(AboutSmartPhoneAppImages, AboutSmartPhoneAppAdminSite)
admin.site.register(AboutSmartPhoneAppSpecification, AboutSmartPhoneAppSpecificationAdminSite)
admin.site.register(About, AboutAdminSite)
admin.site.register(AboutVideo, AboutVideoAdminSite)
admin.site.register(ConnectivityDevices, ConnectivityDevicesAdminSite)
admin.site.register(HowItWorks, HowItWorksAdminSite)
admin.site.register(FAQs, FAQsAdminSite)
