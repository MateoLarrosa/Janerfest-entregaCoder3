from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# Create your models here.
class InfoExtra(models.Model):
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='infoextra')
    mail = models.EmailField()
    link_a_pagina =  models.URLField( max_length=400)
    descripción = RichTextField()
    
    def __str__(self):
        return f'{self.nombre}. {self.apellido} {self.avatar}.'