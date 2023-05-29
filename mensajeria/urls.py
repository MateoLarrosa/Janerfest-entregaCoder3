from django.urls import path
from . import views

app_name = 'mensajeria'

urlpatterns = [
    path('comentarios/', views.mostrar_comentarios, name='mostrar_comentarios'),
    path('comentario/responder/<int:comentario_id>/', views.responder_comentario, name='responder_comentario'),
    path('comentario/crear/', views.crear_comentario, name='crear_comentario'),
]
