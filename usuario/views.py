from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from usuario.models import InfoExtra
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView

from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import Template,Context,loader

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


from usuario.forms import MiFormularioDeCreacion,EdicionPerfil,MiFormularioCambiocontrasenia
# Create your views here.
def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contrasenia = formulario.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario,password = contrasenia)
            django_login(request,usuario)
            InfoExtra.objects.get_or_create(user=request.user)
            return redirect('entradas:index')
        else: 
            return render(request,'usuarios/login.html',{'formulario':formulario})
    formulario = AuthenticationForm()
    return render(request,'usuarios/login.html',{'formulario':formulario})

def registro(request):
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuario:login')
        else: 
            return render(request,'usuarios/registro.html',{'formulario':formulario})
    formulario = MiFormularioDeCreacion()
    return render(request,'usuarios/registro.html',{'formulario':formulario})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            user = formulario.save()
            user.infoextra.nombre = formulario.cleaned_data['nombre']
            user.infoextra.mail = formulario.cleaned_data['email']
            user.infoextra.descripcion = formulario.cleaned_data['descripcion']
            user.infoextra.link_a_pagina = formulario.cleaned_data['url']
            if formulario.cleaned_data.get('avatar'):
                user.infoextra.avatar = formulario.cleaned_data['avatar']
            user.infoextra.save()
            return redirect('usuario:editar_perfil')
        else:
            return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})
    formulario = EdicionPerfil(initial={'avatar': request.user.infoextra.avatar,
    'nombre': request.user.infoextra.nombre,
    'apellido': request.user.infoextra.apellido,
    'email': request.user.infoextra.mail,
    'descripcion': request.user.infoextra.descripcion,
    'link_a_pagina': request.user.infoextra.link_a_pagina,},
                               instance=request.user)
    return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})


class Cambiocontrasenia(PasswordChangeView):
    form_class = MiFormularioCambiocontrasenia
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuario:editar_perfil')
    
class MostrarPerfil(LoginRequiredMixin, DetailView):
    model = InfoExtra
    template_name = "usuarios/mostrar_perfil.html"

    def get_object(self, queryset=None):
        # Obtener el objeto InfoExtra asociado al usuario actual
        return self.request.user.infoextra

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['InfoExtra'] = self.get_object()  # Pasar el objeto InfoExtra al contexto
        return context