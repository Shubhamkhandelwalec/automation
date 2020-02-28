from django.contrib import admin
from .models import *
from .forms import *
# Register your models here.


class OurProductsAdminsite(admin.ModelAdmin):
    list_display = ('id', 'product_title', 'created_at', 'created_at')


class ProductImagesAdminsite(admin.ModelAdmin):
    def our_products_name(self, obj):
        return obj.product_id.product_title

    def product_images(self, obj):
        return obj.product_images.name
    list_display = ('id', 'product_images', 'our_products_name', 'created_at')
    form = ProductImagesForm


admin.site.register(OurProducts)
admin.site.register(ProductImages)
