from django.shortcuts import render
from .models import *

# Create your views here.
def About_Ficus(request):
    return render(request, 'about_ficus.html')


def About_SmartPhoneApp(request):
    about_smart_phone_app_title = AboutSmartPhoneAppTitle.objects.get()
    about_smart_phone_app_images = AboutSmartPhoneAppImages.objects.all()
    about_smart_phone_app_specification = AboutSmartPhoneAppSpecification.objects.all()
    return render(request, 'about_smartphone_app.html',
                  {'about_smart_phone_app_title': about_smart_phone_app_title,
                   'about_smart_phone_app_images': about_smart_phone_app_images,
                   'about_smart_phone_app_specification': about_smart_phone_app_specification})


def About_AmazonAlexa(request):
    return render(request, 'about_amazon_alexa.html')


def About_GoogleHome(request):
    return render(request, 'about_googlehome.html')


def About_HowItWork(request):
    return render(request, 'about_howit_work.html')


def About_Faq(request):
    return render(request, 'about_faqs.html')