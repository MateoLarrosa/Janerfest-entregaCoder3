from django import forms
from ckeditor.fields import RichTextFormField

class FormularioComprarEntradas(forms.Form):
    OPCIONES_METODO_PAGO = [('efectivo', 'Efectivo'), ('mercadopago', 'MercadoPago')]

    nombre = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su nombre'}))
    mail = forms.CharField(max_length=40, widget=forms.TextInput(attrs={'placeholder': 'Ingrese su mail'}))
    cant_entradas = forms.IntegerField()
    metodo_pago = forms.ChoiceField(choices=OPCIONES_METODO_PAGO)
    opinion = RichTextFormField(
        widget=forms.TextInput(attrs={'placeholder': 'Ingrese su opinión aquí'}),
        help_text='Deje su opinión sobre la edición del janerfest 2022 y cómo se enteró de ella.'
    )

    
class BuscarCliente(forms.Form):
    nombre = forms.CharField(max_length=20,required=False)
    #hijos_participantes = forms.CharField(max_length=2,required=False)
    #cant_entradas = forms.IntegerField(required=False)
    
class ModificarCompra(forms.Form):
    nombre = forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Inrese su nombre'}))
    mail = forms.CharField(max_length=40,widget=forms.TextInput(attrs={'placeholder': 'Inrese su mail'}))
    cant_entradas = forms.IntegerField()
    opinion = RichTextFormField()
