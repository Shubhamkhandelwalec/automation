from django.core.validators import RegexValidator
from django import forms
from .models import *
from django.http import JsonResponse

class user_ifvalid(forms.Form):

    firstname = forms.CharField(required=True)
    lastname = forms.CharField(required=True)
    username = forms.CharField(required=True)
    mobile = forms.CharField( required=True)
    email = forms.EmailField( required=True)
    dob = forms.DateTimeField(required=True)
    image = forms.FileField(required=True)



    class Meta:
        model = User
        fields = ('firstname', 'lastname','patient_uniqueid', 'mobile', 'email','dob','image')

    def clean(self):
        print("comes in forms")
        cleaned_data = super(user_ifvalid, self).clean()
        print(cleaned_data)

        # if User.objects.filter(first_name=firstname).exists():
        #     raise forms.ValidationError("Duplicate entry")
        return cleaned_data
#
class useredit_ifvalid(forms.Form):
    username = forms.CharField(required=True)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    # patient_uniqueid = forms.CharField(required=True)
    mobile = forms.CharField(required=False)
    email = forms.EmailField(required=False)
    dob = forms.DateTimeField(required=False)
    image = forms.FileField(required=False)

    class Meta:
        model = User
        fields =('username','firstname', 'lastname','mobile', 'email', 'dob','image')

    def clean(self):
        cleaned_data = super(useredit_ifvalid,self).clean()
        print("comes in forms")
        return cleaned_data
#
#
# class cmsdelete_ifvalid(forms.Form):
#     title = forms.CharField(required=False)
#     username = forms.CharField(required=True)
#     meta_title = forms.CharField(required=False)
#     sub_title = forms.CharField(required=False)
#     meta_keyword = forms.CharField(required=False)
#     slug = forms.CharField(required=False)
#     meta_description = forms.CharField(required=False)
#     short_description = forms.CharField(required=False)
#     image = forms.FileField(required=False)
#     description = forms.CharField(required=False)
#
#     class Meta:
#         model = Cmspages
#         fields = (
#         'title', 'username', 'meta_title', 'sub_title', 'meta_keyword', 'slug', 'meta_description', 'short_description',
#         'image', 'description')
#
#     def clean(self):
#         cleaned_data = super(cmsdelete_ifvalid,self).clean()
#
#         return cleaned_data