from django.urls import path
# from django.urls import re_path
from . import views

urlpatterns = [

    path('user/add', views.Adduser, name='Adduser'),
    path('user/edit/<int:id>', views.Edituser, name='Edituser'),
#     # path('user/delete/<int:id>', views.Deleteuser, name='Deleteuser'),
#     # path('user/viewuser/<int:id>', views.Viewuser, name='View user'),
#     # path('user/viewuser', views.ViewAllusers),
]