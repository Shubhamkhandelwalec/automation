from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.


class OurProducts(models.Model):
    product_title = models.CharField(max_length=250)
    product_description = RichTextField(max_length=20000)
    Specifications = RichTextField(max_length=20000, help_text='Specifications separate by ;')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    product_amazon_url = models.TextField(max_length=2500)
    product_flipkart_url = models.TextField(max_length=2500)
    product_buy_url = models.TextField(max_length=2500, null=True, blank=True)


class ProductImages(models.Model):
    product_images = models.ImageField(upload_to='ProductImages/')
    product_id = models.ForeignKey(OurProducts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
