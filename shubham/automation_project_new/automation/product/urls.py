from django.urls import path
from . import views

urlpatterns = [

    path('home-automation-kit/', views.home_automation_kit, name='product'),
    path('home-automation-product-detail/<int:id>/', views.home_automation_product_detail, name='product'),
    path('water-level-controller/', views.water_level_controller, name='product'),
]