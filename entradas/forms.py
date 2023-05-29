from django import forms
from ckeditor.fields import RichTextFormField

class FormularioComprarEntradas(forms.Form):
    OPCIONES_METODO_PAGO = [('efectivo', 'Efectivo'), ('mercadopago', 'MercadoPago')]

    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    mail = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su mail'}))
    cant_entradas = forms.IntegerField()
    metodo_pago = forms.ChoiceField(choices=OPCIONES_METODO_PAGO)
    opinion = forms.Media()
    imagen = forms.ImageField()

class ModificarCompra(forms.Form):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Inrese su nombre'}))
    mail = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Inrese su mail'}))
    cant_entradas = forms.IntegerField()
    opinion = forms.Media()
