from django import forms

class FormularioComprarEntradas(forms.Form):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Inrese su nombre'}))
    mail = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Inrese su mail'}))
    cant_entradas = forms.IntegerField()
    hijos_participantes = forms.CharField(max_length=2,widget=forms.TextInput(attrs={'placeholder': 'Inrese si-no'}))
class BuscarCliente(forms.Form):
    nombre = forms.CharField(max_length=20,required=False)
    #hijos_participantes = forms.CharField(max_length=2,required=False)
    #cant_entradas = forms.IntegerField(required=False)
    
class ModificarCompra(forms.Form):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Inrese su nombre'}))
    mail = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Inrese su mail'}))
    cant_entradas = forms.IntegerField()
    hijos_participantes = forms.CharField(max_length=2,widget=forms.TextInput(attrs={'placeholder': 'Inrese si-no'}))