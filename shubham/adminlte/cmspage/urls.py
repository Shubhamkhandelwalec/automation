from django.urls import path
# from django.urls import re_path
from . import views

urlpatterns = [

    path('cmspages/add', views.Addcms, name='Addcms'),
    path('cmspages/edit/<int:id>', views.Editcms, name='Editcms'),
    path('cmspages/delete/<int:id>', views.Deletecms, name='Deletecms'),
    path('cmspages/viewuser/<int:id>', views.Viewuser, name='View user'),
    path('cmspages/viewuser', views.ViewAllusers),
    path('api/v1/user/login',views.Loginuser,name='login user'),
]