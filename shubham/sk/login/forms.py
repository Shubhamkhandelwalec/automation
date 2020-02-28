from django import forms
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from .models import  *

class Signup(forms.Form):
    username = forms.CharField(min_length=2,max_length=100,required=True,)
    fullname = forms.CharField(min_length=2, max_length=100, required=True)

    email = forms.EmailField(min_length=5, max_length=100, required=True)
    # password = forms.CharField(min_length=8, max_length=20, required=True, widget=(forms.PasswordInput(attrs={'placeholder': 'password'})), validators=[
    #     RegexValidator(regex=r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")])
    # confirm_password = forms.CharField(widget=(forms.PasswordInput(attrs ={'placeholder': 'password'})), required=True)
    # pics = forms.ImageField(required= True)


    # class Meta:
    #     model = Registration
    #     fields = ('username', 'fullname','email')
    #
    # def clean(self):
    #     cleaned_data = super(Signup, self).clean()
    #     password = cleaned_data.get("password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if password != confirm_password:
    #         raise forms.ValidationError(
    #             "password and confirm password does not match"
    #         )


class LoginForms(forms.Form):
    username = forms.CharField(max_length=100,required=True)
    password = forms.CharField( max_length=200, required=True)

    class Meta:
        model = Registration
        fields = ('username','password')

class Updatedform(forms.Form):
    # username = forms.CharField(min_length=5,max_length=10)
    # full_name = forms.CharField(min_length=2, max_length=50,)
    # email = forms.EmailField(min_length=8, max_length=50)
    password = forms.CharField(required=True)
    # new_password = forms.CharField(min_length=8, max_length=20, widget=(forms.PasswordInput()), validators=[
    #     RegexValidator(regex=r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$")])
    # confirm_password = forms.CharField(widget=(forms.PasswordInput()))
    # pics = forms.ImageField()


    class Meta:
        model = Registration
        fields = ('password',)

    # def clean(self):
    #     cleaned_data = super(Updatedform, self).clean()
    #     new_password = cleaned_data.get("old_password")
    #     confirm_password = cleaned_data.get("confirm_password")
    #
    #     if new_password != confirm_password:
    #         raise forms.ValidationError(
    #             "new password and confirm password does not match"
    #         )
class Verification(forms.Form):
    password = forms.CharField(min_length=2, max_length=100, required=True,
                               widget=(forms.PasswordInput()))
    confirm_password = forms.CharField(required=True)

    class Meta:
        model = Registration
        fields = ('password', 'confirm_password')

    def clean(self):
        cleaned_data = super(Verification, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm password does not match"
            )