from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('all', all),
    path('create/<uname>/<psw>', create),
    path('delete/<uname>', delete),
    path('uname/<int:id>', get),
    path('uname/<str:username>', get_username, name = 'get_username'),
    path('password/<str:password>', get_password),
]
