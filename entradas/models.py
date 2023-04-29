from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
# Create your models here.

class Cliente(models.Model):
    OPCIONES_METODO_PAGO = [
        ('efectivo', 'Efectivo'),
        ('mercadopago', 'MercadoPago'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20)
    mail = models.CharField(max_length=30,)
    cant_entradas = models.IntegerField()
    metodo_pago = models.CharField(max_length=20, choices=OPCIONES_METODO_PAGO)
    opinion = RichTextField()
    created_at = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return f'{self.nombre}. {self.cant_entradas} entradas compradas el {self.created_at}.'