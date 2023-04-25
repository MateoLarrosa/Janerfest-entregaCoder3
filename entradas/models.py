from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Cliente(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1)
    nombre = models.CharField(max_length=20)
    mail = models.CharField(max_length=30,)
    cant_entradas = models.IntegerField()
    hijos_participantes = models.CharField(max_length=2)
    
    def get_queryset(self):
    # Obtener las instancias del modelo Cliente correspondientes al usuario logueado
        return Cliente.objects.filter(user=self.request.user)

    def __str__(self):
        return f'{self.nombre}. {self.cant_entradas} entradas compradas.'