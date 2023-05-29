from django.db import models
from ckeditor.fields import RichTextField

class Comentario(models.Model):
    emisor = RichTextField()
    receptor = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='respuestas')
    
    def tiene_respuestas(self):
        return self.respuestas.exists()
