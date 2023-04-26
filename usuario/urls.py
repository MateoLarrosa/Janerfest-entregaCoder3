from django.urls import path
from usuario import views
from django.contrib.auth.views import LogoutView
app_name = 'usuario'

urlpatterns = [
    path('',views.login, name='login'),
    path('registro/',views.registro, name='registro'),
    path('perfil/editar/',views.editar_perfil, name='editar_perfil'),
    path('logout/',LogoutView.as_view(template_name = 'usuarios/logout.html'), name='logout'),
    path('cambiar-contraseña/',views.CambioContraseña.as_view(), name='cambiar_contraseña')
] 
