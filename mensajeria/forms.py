from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['emisor']

class RespuestaForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['emisor']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['emisor'].label = 'Respuesta'

