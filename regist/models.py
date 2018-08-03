from django.db import models

class member(models.Model):
    id = models.CharField(max_length=25,primary_key=True)
    password = models.CharField(max_length=25)
    name = models.CharField(max_length=25)
