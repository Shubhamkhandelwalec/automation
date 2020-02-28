from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/contactus/', views.contact_us,  name='contact_us'),
]