from service_objects.services import Service
from django import forms
from django.contrib.auth.models import User

class Userservice(Service):
    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email= forms.EmailField()
    password= forms.CharField()

    def process(self):
        u = User(username=self.cleaned_data['username'], first_name=self.cleaned_data['first_name'],
                 last_name=self.cleaned_data['last_name'], email=self.cleaned_data['email'], is_superuser=True,
                 is_staff=True, is_active=True)
        u.set_password(self.cleaned_data['password'])
        u.save()

class Editservice(Service):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email= forms.EmailField(required=False)
    id =  forms.IntegerField(required=True)


    def process(self):
        detail = User.objects.get(username=self.cleaned_data['username'],id=self.cleaned_data['id'])

        if self.cleaned_data['first_name'] != "":
            detail.first_name = self.cleaned_data['first_name']
        if self.cleaned_data['last_name'] != "":
            detail.last_name = self.cleaned_data['last_name']
        if self.cleaned_data['email'] != "":
            detail.email = self.cleaned_data['email']
        detail.save()

class Deleteservice(Service):
    username = forms.CharField(required=True)
    first_name = forms.CharField(required=False)
    last_name = forms.CharField(required=False)
    email= forms.EmailField(required=False)
    id = forms.IntegerField(required=True)


    def process(self):
        detail = User.objects.get(username=self.cleaned_data['username'],id=self.cleaned_data['id'])
        detail.delete()


