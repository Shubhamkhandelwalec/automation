from service_objects.services import Service
from django import forms
from random import randint
from .models import *

class addcms(Service):

    username = forms.CharField()

    title = forms.CharField()
    meta_title = forms.CharField()
    sub_title = forms.CharField()
    meta_keyword = forms.CharField()
    slug = forms.CharField()
    meta_description = forms.CharField()
    short_description = forms.CharField()
    image = forms.ImageField()
    description = forms.CharField()
    # uniqueid = forms.IntegerField()
    def process(self):
        print("<><><><><><>",self.cleaned_data['username'])
        u = Cmspages(username=self.cleaned_data['username'], title=self.cleaned_data['title'],
                 meta_title=self.cleaned_data['meta_title'], sub_title=self.cleaned_data['sub_title'],
                     meta_keyword=self.cleaned_data['meta_keyword'], slug=self.cleaned_data['slug'],
                 meta_description=self.cleaned_data['meta_description'], short_description=self.cleaned_data['short_description'],
                     image=self.cleaned_data['image'], description=self.cleaned_data['description'],
                 uniqueid= randint(10**(9-1),(10**9)-1))

        u.save()

class editcms(Service):
    username = forms.CharField()
    title = forms.CharField(required=False)
    meta_title = forms.CharField(required=False)
    sub_title = forms.CharField(required=False)
    meta_keyword = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    meta_description = forms.CharField(required=False)
    short_description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    description = forms.CharField(required=False)

    def process(self):
        detail = Cmspages.objects.get(username=self.cleaned_data['username'])
        print("des", self.cleaned_data['short_description'])
        print("image", self.cleaned_data['image'])
        if self.cleaned_data['title'] != "":
            detail.title = self.cleaned_data['title']
        if self.cleaned_data['meta_title'] != "":
            detail.meta_title = self.cleaned_data['meta_title']
        if self.cleaned_data['sub_title'] != "":
            detail.sub_title = self.cleaned_data['sub_title']
        if self.cleaned_data['meta_keyword'] != "":
            detail.meta_keyword = self.cleaned_data['meta_keyword']
        if self.cleaned_data['slug'] != "":
            detail.slug = self.cleaned_data['slug']
        if self.cleaned_data['meta_description'] != "":
            detail.meta_description = self.cleaned_data['meta_description']
        if self.cleaned_data['short_description'] != "":
            print("des", self.cleaned_data['short_description'])
            detail.short_description = self.cleaned_data['short_description']
        if self.cleaned_data['image'] != None:
            detail.image = self.cleaned_data['image']
        if self.cleaned_data['description'] != "":
            detail.description = self.cleaned_data['description']
        detail.save()


class deletecms(Service):
    username = forms.CharField()
    title = forms.CharField(required=False)
    meta_title = forms.CharField(required=False)
    sub_title = forms.CharField(required=False)
    meta_keyword = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    meta_description = forms.CharField(required=False)
    short_description = forms.CharField(required=False)
    image = forms.ImageField(required=False)
    description = forms.CharField(required=False)


    def process(self):
        detail = Cmspages.objects.get(username=self.cleaned_data['username'])
        detail.delete()


