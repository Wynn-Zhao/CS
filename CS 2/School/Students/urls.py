from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('delete/all', delete_all),
    path('exit/', exit),
    path('register/', register),
    path('login/', login),
    path('dashboard/', dashboard),
    path('<str:firstname>/', get_student, name = 'get_student'),
    path('<str:firstname>/change', change, name = 'change'),
    path('delete_account/', delete_account)
]