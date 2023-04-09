from django.db import models

# Create your models here.

class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    mail = models.CharField(max_length=30,)
    cant_entradas = models.IntegerField()
    
    def __str__(self):
        return f'Soy {self.nombre}, mi mail es {self.mail} y compre {self.cant_entradas} entradas'