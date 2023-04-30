from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InfoExtra(models.Model):
    nombre = models.TextField(max_length=20)
    apellido = models.TextField(max_length=20)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='infoextra')