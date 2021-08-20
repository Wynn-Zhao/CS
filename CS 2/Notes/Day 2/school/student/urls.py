from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index),
    path('bye/', bye),
    path('add/', add),
    path('all/', students),
    path('student/<id>', student),
    path('year/<year>', student_by_year),
    path('session/name', my_name)
]