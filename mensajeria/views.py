from django.shortcuts import render, redirect
from .models import Comentario
from .forms import ComentarioForm, RespuestaForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy

@login_required
def mostrar_comentarios(request):
    comentarios = Comentario.objects.all()
    respuesta_form = RespuestaForm()
    return render(request, 'mensajeria/mostrar_comentarios.html', {'comentarios': comentarios, 'respuesta_form': respuesta_form})

@login_required
def responder_comentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    if request.method == 'POST':
        respuesta_form = RespuestaForm(request.POST)
        if respuesta_form.is_valid():
            respuesta = respuesta_form.cleaned_data['emisor']
            Comentario.objects.create(emisor=respuesta, receptor=comentario)
            return redirect('mensajeria:mostrar_comentarios')
    else:
        respuesta_form = RespuestaForm()
    return render(request, 'mensajeria/responder_comentario.html', {'comentario': comentario, 'respuesta_form': respuesta_form})

@login_required
def crear_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mensajeria:mostrar_comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'mensajeria/crear_comentario.html', {'form': form})

class CancelarCompra(LoginRequiredMixin,DeleteView):
    model = Comentario
    template_name = "mensajeria/mostrar_comentarios.html"
    success_url = reverse_lazy('mensajeria:mostrar_comentarios')
