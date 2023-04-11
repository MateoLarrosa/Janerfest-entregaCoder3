from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from entradas.models import Cliente
from entradas.forms import CreacionClienteFormulario,BuscarCliente

# Create your views here.

def index(request):
    return render(request,r'entradas/index.html')

def sacar_entradas(request):
    
    if request.method == "POST":
        formulario = CreacionClienteFormulario(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
                        
        cliente = Cliente(nombre=datos_correctos['nombre'], mail = datos_correctos['mail'], cant_entradas= datos_correctos['cant_entradas'], hijos_participantes= datos_correctos['hijos_participantes'])
        cliente.save()
        
        return redirect('entradas:lista-clientes')
        
    formulario = CreacionClienteFormulario
    return render(request,r'entradas/comprar_entradas.html',{'formulario':formulario})


def lista_clientes(request):
    cliente_a_buscar = request.GET.get('nombre',None)
    
    if cliente_a_buscar:
        clientes = Cliente.objects.filter(nombre__icontains=cliente_a_buscar)
    else:
        clientes = Cliente.objects.all()
        
    formulario_busqueda = BuscarCliente()
    return render(request,r'entradas/lista_clientes.html',{'clientes':clientes,'formulario':formulario_busqueda})


def quienes_somos(request):
    return render(request,r'entradas/quienes_somos.html')