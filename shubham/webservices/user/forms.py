from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.http import JsonResponse

class user_ifvalid(forms.Form):
    username = forms.CharField( required=True)
    firstname = forms.CharField(required=True)
    lastname = forms.CharField( required=True)
    email = forms.EmailField( required=True)
    password = forms.CharField(required=True)


    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email','password')

    def clean(self):
        cleaned_data = super(user_ifvalid, self).clean()
        clean_username = cleaned_data.get('username')

        if User.objects.filter(username=clean_username).exists():
            raise forms.ValidationError("Duplicate entry")
        return cleaned_data


class editform_ifvalid(forms.Form):
    username = forms.CharField(required=True)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean(self):
        cleaned_data = super(editform_ifvalid,self).clean()
        return cleaned_data

class deleteform_ifvalid(forms.Form):
    username = forms.CharField(required=True)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    email = forms.CharField(required=False)

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email')

    def clean(self):
        cleaned_data = super(deleteform_ifvalid,self).clean()

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




