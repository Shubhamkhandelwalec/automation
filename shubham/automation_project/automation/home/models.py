from django.db import models


class HomeImage(models.Model):
    home_image = models.ImageField(upload_to='home/', default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)




