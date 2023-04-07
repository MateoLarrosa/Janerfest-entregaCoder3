from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    mail = models.CharField(max_length=30,)
    cant_entradas = models.IntegerField()