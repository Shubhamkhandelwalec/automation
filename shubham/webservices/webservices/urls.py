"""webservices URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from user.views import *
from article.views import *

urlpatterns = [

    # //////////////////routes fo users///////////
    path('admin/', admin.site.urls),
    path('api/v1/user/adduser',Adduser,name = 'Add user'),
    path('api/v1/user/edituser/<int:id>', Edituser,name = 'Edit user'),
    path('api/v1/user/deleteuser/<int:id>',Deleteuser,name = 'Delete user'),
    path('api/v1/user/viewuser/<int:id>', Viewuser, name='View user'),
    path('api/v1/user',ViewAllusers),
    path('api/v1/user/login',Loginuser,name='login user'),

    #/////// routes of articles //////////

    path('api/v1/article/addarticle',Addarticle,name = 'Add article'),
    path('api/v1/article/editarticle/<int:id>',Editarticle,name='Edit article'),
    path('api/v1/article/deletearticle/<int:id>',Deletearticle,name='Delete article'),
    path('api/v1/article/viewarticle/<int:id>', Viewarticle, name='View Article'),
    path('api/v1/article',ViewAllArticle),

]
