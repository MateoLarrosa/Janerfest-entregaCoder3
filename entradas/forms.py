from django import froms

class CreacionClienteFormulario(forms.form):
    nombre = form.CharField(max_length=20)
    mail = form.CharField(max_length=40)
    cant_entradas = form.IntergerField()

class BuscarCliente(forms.form):
    nombre = form.CharField(max_length=20)
    cant_entradas = form.IntergerField()