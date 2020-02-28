from django import forms
from .models import *


class ContactUsForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    city = forms.CharField(required=True)

    class Meta:
        model = ContactUs
        fields = ('name', 'phone', 'email', 'city')
