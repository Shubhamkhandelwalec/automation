from django.urls import path
from . import views

urlpatterns = [

    path('aboutficus/', views.About_Ficus, name='About Ficus'),
    path('about_smartphone_app/', views.About_SmartPhoneApp, name='About Smartphoneapp'),
    path('about_amazon_echo_alexa/', views.About_AmazonAlexa, name='About Amazon Alexa&Echo'),
    path('about_google_home/', views.About_GoogleHome, name='About GoogleHome'),
    path('about_how_it_work/', views.About_HowItWork, name='About HowItWork'),
    path('FAQs/', views.About_Faq, name='About Faq'),


]