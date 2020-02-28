from django.core.validators import RegexValidator
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.http import JsonResponse

class cms_ifvalid(forms.Form):
    title = forms.CharField(required=True)
    username = forms.CharField(required=True)
    meta_title = forms.CharField(required=True)
    sub_title = forms.CharField( required=True)
    meta_keyword = forms.CharField( required=True)
    slug = forms.CharField(required=True)
    meta_description = forms.CharField(required=True)
    short_description = forms.CharField(required=True)
    image = forms.FileField(required=True)
    description = forms.CharField(required=True)



    class Meta:
        model = Cmspages
        fields = ('title', 'username','meta_title', 'sub_title', 'meta_keyword','slug','meta_description', 'short_description', 'image', 'description')

    def clean(self):
        cleaned_data = super(cms_ifvalid, self).clean()
        username = cleaned_data.get('username')

        if Cmspages.objects.filter(username=username).exists():
            raise forms.ValidationError("Duplicate entry")
        return cleaned_data

class cmsedit_ifvalid(forms.Form):
    title = forms.CharField(required=False)
    username = forms.CharField(required=True)
    meta_title = forms.CharField(required=False)
    sub_title = forms.CharField(required=False)
    meta_keyword = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    meta_description = forms.CharField(required=False)
    short_description = forms.CharField(required=False)
    image = forms.FileField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Cmspages
        fields =('title', 'username','meta_title', 'sub_title', 'meta_keyword','slug','meta_description', 'short_description', 'image', 'description')

    def clean(self):
        cleaned_data = super(cmsedit_ifvalid,self).clean()
        print("comes in forms")
        return cleaned_data


class cmsdelete_ifvalid(forms.Form):
    title = forms.CharField(required=False)
    username = forms.CharField(required=True)
    meta_title = forms.CharField(required=False)
    sub_title = forms.CharField(required=False)
    meta_keyword = forms.CharField(required=False)
    slug = forms.CharField(required=False)
    meta_description = forms.CharField(required=False)
    short_description = forms.CharField(required=False)
    image = forms.FileField(required=False)
    description = forms.CharField(required=False)

    class Meta:
        model = Cmspages
        fields = (
        'title', 'username', 'meta_title', 'sub_title', 'meta_keyword', 'slug', 'meta_description', 'short_description',
        'image', 'description')

    def clean(self):
        cleaned_data = super(cmsdelete_ifvalid,self).clean()

        return cleaned_data

class userlogin_ifvalid(forms.Form):
    username = forms.CharField( required=True)
    password = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ('username', 'password')

    def clean(self):
        cleaned_data = super(userlogin_ifvalid, self).clean()
        # clean_username = cleaned_data.get('username')

        return cleaned_data

