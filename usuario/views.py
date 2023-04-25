from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth import authenticate, login as django_login
from django.shortcuts import redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from usuario.models import InfoExtra
from django.urls import reverse_lazy

from usuario.forms import MiFormularioDeCreacion,EdicionPerfil
# Create your views here.
def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            nombre_usuario = formulario.cleaned_data.get('username')
            contraseña = formulario.cleaned_data.get('password')
            usuario = authenticate(username = nombre_usuario,password = contraseña)
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
            formulario = EdicionPerfil(request.POST,request.FILES,instance=request.user)
            
            if formulario.is_valid():
                if formulario.cleaned_data.get('avatar'):
                    request.user.infoextra.avatar = formulario.cleaned_data.get('avatar')
                    
                request.user.infoextra.save()
                formulario.save()
                return redirect('usuario:editar_perfil')
            
            else: 
                return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})
            
        formulario = EdicionPerfil(initial = {'avatar':request.user.infoextra.avatar},instance =request.user)
        return render(request,'usuarios/editar_perfil.html',{'formulario':formulario})


class CambioContrasenia(PasswordChangeView):
    template_name = 'usuarios/cambiar_contrasenia.html'
    success_url = reverse_lazy('usuarios:editar_perfil')