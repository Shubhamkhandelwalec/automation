from django import forms
from .models import *
from django.forms import BaseModelForm, ModelForm


class TitleNameField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.title_name)


class AboutSmartPhoneAppForm(ModelForm):
    title_id = TitleNameField(queryset=AboutSmartPhoneAppTitle.objects.all(), required=True)
    app_images = forms.ImageField(required=True)

    class Meta:
        model = AboutSmartPhoneAppImages
        fields = ('title_id', 'app_images')


class AboutSmartPhoneAppSpecificationForm(ModelForm):
    about_smart_phone_app = TitleNameField(queryset=AboutSmartPhoneAppTitle.objects.all(), required=True)
    specification_title = forms.CharField(required=True)
    specification_logo_class = forms.CharField(required=True)

    class Meta:
        model = AboutSmartPhoneAppSpecification
        fields = ('about_smart_phone_app', 'specification_title', 'specification_logo_class',
                  'specification_description')
