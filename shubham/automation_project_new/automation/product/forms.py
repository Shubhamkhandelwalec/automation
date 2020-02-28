from django import forms
from .models import *


class OurProductField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return "{}".format(obj.product_title)


class ProductImagesForm(forms.Form):
    product_images = forms.ImageField(required=True)
    product_id = OurProductField(queryset=OurProducts.objects.all(), required=True)

    class Meta:
        model = ProductImages
        fields = ('product_images', 'product_id')
