from django.urls import path
from entradas import views

app_name = 'entradas'

urlpatterns = [
    path('',views.index,name='index'),
    path('comprar-entradas/',views.sacar_entradas,name='entradas'),
    path('quienes-somos/',views.quienes_somos,name='quienes-somos'),
    path('lista-clientes/',views.lista_clientes,name='lista-clientes'),
]