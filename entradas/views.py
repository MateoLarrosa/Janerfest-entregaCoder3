from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from entradas.models import Cliente
from entradas.forms import FormularioComprarEntradas,BuscarCliente,ModificarCompra

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
""" 
def sacar_entradas(request):
    
    if request.method == "POST":
        formulario = FormularioComprarEntradas(request.POST)
        
        if formulario.is_valid():
            datos_correctos = formulario.cleaned_data
                        
        cliente = Cliente(nombre=datos_correctos['nombre'], mail = datos_correctos['mail'], cant_entradas= datos_correctos['cant_entradas'], hijos_participantes= datos_correctos['hijos_participantes'])
        cliente.save()
        
        return redirect('entradas:estado_entradas')
        
    formulario = FormularioComprarEntradas
    return render(request,r'entradas/comprar_entradas.html',{'formulario':formulario})


def estado_de_entradas(request):
    cliente_a_buscar = request.GET.get('nombre',None)
    
    if cliente_a_buscar:
        clientes = Cliente.objects.filter(nombre__icontains=cliente_a_buscar)
    else:
        clientes = print("esperando consulta...")
        
    formulario_busqueda = BuscarCliente()
    return render(request,r'entradas/estado_de_entradas.html',{'clientes':clientes,'formulario':formulario_busqueda})

def cancelar_compra(request,id_cliente):
    cancelar_compra = Cliente.objects.get(id= id_cliente)
    cancelar_compra.delete()
    return redirect('entradas:entradas')

def mostrar_compra(request,id_cliente):
    compra_a_mostrar = Cliente.objects.get(id=id_cliente)
    return render(request,'entradas/mostrar_compra.html',{'compra_a_mostrar':compra_a_mostrar,'id_cliente': id_cliente})

def modificar_compra(request,id_cliente):
    modificar_compra = Cliente.objects.get(id= id_cliente)
    
    if request.method == "POST":
        formulario = ModificarCompra(request.POST)
        if formulario.is_valid():
            data_limpia = formulario.cleaned_data
            modificar_compra.nombre = data_limpia['nombre']
            modificar_compra.mail = data_limpia['mail']
            modificar_compra.cant_entradas = data_limpia['cant_entradas']
            modificar_compra.hijos_participantes = data_limpia['hijos_participantes']
            modificar_compra.save()
            return redirect('entradas:estado_entradas')
        else:
            return render(request,'entradas/modificar_compra.html',{'formulario': formulario,'id_cliente': id_cliente})
            
        
    formulario = ModificarCompra(initial={'nombre':modificar_compra.nombre,'mail':modificar_compra.mail,'cant_entradas': modificar_compra.cant_entradas,'hijos_participantes':modificar_compra.hijos_participantes})
    return render(request,'entradas/modificar_compra.html',{'formulario': formulario,'id_cliente': id_cliente})
    
 """
def index(request):
    return render(request,r'entradas/index.html')
 
@login_required
def quienes_somos(request):
    return render(request,r'entradas/quienes_somos.html')


#CBV

class EstadoDeEntradas(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = "entradas/CBV/estado_de_entradas.html"
    success_url = '/entradas/'
    fields = ['nombre','created_at']



class ComprarEntradas(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "entradas/CBV/comprar_entradas.html"
    success_url = '/entradas/'
    fields = ['nombre', 'mail', 'cant_entradas', 'opinion','metodo_pago']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    
class ModificarCompra(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "entradas/CBV/modificar_compra.html"
    success_url ='/entradas/'
    fields = ['nombre','mail','cant_entradas','opinion']
    
class CancelarCompra(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "entradas/CBV/cancelar_compra.html"
    success_url ='/entradas/'

class MostrarCompra(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "entradas/CBV/mostrar_compra.html"
    success_url ='/entradas/'