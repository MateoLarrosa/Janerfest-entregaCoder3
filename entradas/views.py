from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from entradas.models import Cliente
from entradas.forms import FormularioComprarEntradas,ModificarCompra

from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.
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
    fields = ['nombre','created_at','flag']
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['flag'] = False
        for cliente in context['object_list']:
            if cliente.user == self.request.user:
                context['flag'] = True
                break
        return context


class ComprarEntradas(LoginRequiredMixin, CreateView):
    model = Cliente
    template_name = "entradas/CBV/comprar_entradas.html"
    success_url = reverse_lazy('entradas:index')
    fields = ['nombre', 'mail', 'cant_entradas', 'opinion', 'metodo_pago','imagen']

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        self.object.realizar_compra()  # Llama al método realizar_compra() en la instancia de Cliente
        return response

    

    
class ModificarCompra(LoginRequiredMixin,UpdateView):
    model = Cliente
    template_name = "entradas/CBV/modificar_compra.html"
    success_url = reverse_lazy('entradas:index')
    fields = ['nombre', 'mail', 'cant_entradas', 'opinion','metodo_pago']
    
class CancelarCompra(LoginRequiredMixin,DeleteView):
    model = Cliente
    template_name = "entradas/CBV/cancelar_compra.html"
    success_url = reverse_lazy('entradas:index')

class MostrarCompra(LoginRequiredMixin,DetailView):
    model = Cliente
    template_name = "entradas/CBV/mostrar_compra.html"
    success_url = reverse_lazy('entradas:index')
    fields = ['nombre', 'mail', 'cant_entradas', 'opinion','metodo_pago','imagen']