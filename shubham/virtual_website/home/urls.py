from django.urls import path
from . import views
urlpatterns= [
    path('index/',views.index),
    path('rooms/',views.room),
    path('about/',views.about),
    path('blog/',views.blog),

]