from django.db import models

class Student(models.Model):
    firstname = models.CharField(max_length = 20)
    lastname = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)
    origin_country = models.CharField(max_length = 56)
