from service_objects.services import Service
from django import forms
from django.contrib.auth.models import User
from .models import *

class articleadd(Service):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.FileField()
    username = forms.CharField()

    def process(self):
        print("final",self.cleaned_data['username'])
        detail = User.objects.get(username=self.cleaned_data['username'])

        u = Article(title=self.cleaned_data['title'],description= self.cleaned_data['description'],image=self.cleaned_data['image'],userid=detail)
        u.save()

class articledit(Service):
    title = forms.CharField()
    description = forms.CharField()
    image = forms.FileField()
    articleid = forms.IntegerField()

    def process(self):
        detail = Article.objects.get(id=self.cleaned_data['articleid'])


        if self.cleaned_data['title'] != "":
            detail.title = self.cleaned_data['title']
        if self.cleaned_data['description'] != "":
            detail.description = self.cleaned_data['description']
        if self.cleaned_data['image'] != "":
            detail.image = self.cleaned_data['image']
        detail.save()

class articldetete(Service):
    articleid = forms.IntegerField()

    def process(self):
        detail = Article.objects.get(id=self.cleaned_data['articleid'])
        detail.delete()

