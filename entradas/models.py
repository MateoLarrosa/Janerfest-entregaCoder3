from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    mail = models.CharField(max_length=30,)
    cant_entradas = models.IntegerField()
    hijos_participantes = models.CharField(max_length=2)

    def __str__(self):
        return f'{self.nombre}. {self.cant_entradas} entradas compradas.'