from django import froms

class CreacionClienteFormulario(forms.form):
    nombre = forms.CharField(max_length=20)
    mail = forms.CharField(max_length=40)
    cant_entradas = forms.IntergerField()
    hijos_participantes = form.CharField(max_length=2)

class BuscarCliente(forms.form):
    nombre = forms.CharField(max_length=20)
    hijos_participantes = forms.CharField(max_length=2)
    cant_entradas = forms.IntergerField()