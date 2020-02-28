from django.shortcuts import render


# Create your views here.
def About_Ficus(request):
    return render(request, 'about_ficus.html')


def About_SmartPhoneApp(request):
    return render(request, 'about_smartphone_app.html')


def About_AmazonAlexa(request):
    return render(request, 'about_amazon_alexa.html')


def About_GoogleHome(request):
    return render(request, 'about_googlehome.html')


def About_HowItWork(request):
    return render(request, 'about_howit_work.html')


def About_Faq(request):
    return render(request, 'about_faqs.html')