from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.http import JsonResponse
from .models import *


class article_ifvalid(forms.Form):
    title = forms.CharField( required=True)
    description = forms.CharField(required=True)
    image = forms.FileField( required=True)
    username = forms.CharField(required=True)


    class Meta:
        model = Article
        fields = ('title', 'description', 'image','username')

    def clean(self):
        cleaned_data = super(article_ifvalid, self).clean()
        print(">>>>>clean>>",cleaned_data.get('image'))
        return cleaned_data

class articledit_ifvalid(forms.Form):
    title = forms.CharField( required=True)
    description = forms.CharField(required=True)
    image = forms.FileField( required=True)
    userid = forms.IntegerField(required=True)


    class Meta:
        model = Article
        fields = ('title', 'description', 'image','userid')

    def clean(self):
        cleaned_data = super(articledit_ifvalid, self).clean()

        return cleaned_data

class articledelete_ifvalid(forms.Form):

    userid = forms.IntegerField(required=True)


    class Meta:
        model = Article
        fields = ('userid')

    def clean(self):
        cleaned_data = super(articledelete_ifvalid, self).clean()

        return cleaned_data
