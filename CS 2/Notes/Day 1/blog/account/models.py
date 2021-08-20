from django.db import models

class Account(models.Model):
    username = models.CharField(max_length = 10)
    password = models.CharField(max_length = 20)


    def __str__(self):
        return self.username
    def __repr__(self):
        return self.username
