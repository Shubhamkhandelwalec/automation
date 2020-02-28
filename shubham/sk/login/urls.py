from django.urls import path
# from django.urls import re_path
from . import views

urlpatterns = [

    path('register/', views.Register, name='register'),
    path('login/', views.login, name='login'),
    path('users/dashboard/', views.dash , name='dashboard'),
    path('users/addedit/<int:update>',views.edit),
    path('users/del/<int:delid>', views.delete),

    path('register/verify/', views.get),
    # path('user/verified',views.realregistration),
]
handler404 = 'login.views.view_404'