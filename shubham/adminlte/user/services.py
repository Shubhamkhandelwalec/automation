from service_objects.services import Service
from django import forms
from random import randint
from .models import *

class useradd(Service):

    firstname = forms.CharField()
    lastname = forms.CharField()
    username = forms.CharField()
    # patient_uniqueid = forms.CharField()
    mobile = forms.IntegerField()
    email = forms.EmailField()
    dob = forms.DateTimeField()
    image = forms.FileField()
    def process(self):
        print("tyep",type(self.cleaned_data['mobile']))
        u = User( username= self.cleaned_data['username'],first_name=self.cleaned_data['firstname'],
                 last_name=self.cleaned_data['lastname'], uniqueid=randint(10**(9-1),(10**9)-1),
                     mobile=self.cleaned_data['mobile'], email=self.cleaned_data['email'],
                 dob=self.cleaned_data['dob'], image=self.cleaned_data['image'],
                     )

        u.save()

class useredit_service(Service):
    username = forms.CharField()
    id = forms.IntegerField(required=False)
    firstname = forms.CharField(required=False)
    lastname = forms.CharField(required=False)
    # patient_uniqueid = forms.CharField()
    mobile = forms.IntegerField(required=False)
    email = forms.EmailField(required=False)
    dob = forms.DateTimeField(required=False)
    image = forms.FileField(required=False)

    def process(self):
        print("id ==== ",self.cleaned_data['dob'])
        detail = User.objects.get(id=self.cleaned_data['id'],username = self.cleaned_data['username'])

        if self.cleaned_data['firstname'] != "":
            detail.first_name = self.cleaned_data['firstname']
        if self.cleaned_data['lastname'] != "":
            detail.last_name = self.cleaned_data['lastname']
        if self.cleaned_data['mobile'] != None:
            detail.mobile = self.cleaned_data['mobile']
        if self.cleaned_data['email'] != "":
            detail.email = self.cleaned_data['email']
        if self.cleaned_data['dob'] != None:
            detail.dob = self.cleaned_data['dob']
        if self.cleaned_data['image'] != "":
            detail.image = self.cleaned_data['image']

        detail.save()