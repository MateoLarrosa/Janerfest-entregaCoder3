from django.urls import path
from entradas import views

app_name = 'entradas'

urlpatterns = [
    #path('comprar-entradas/',views.sacar_entradas,name='entradas'),
    #path('comprar-entradas/estado/',views.estado_de_entradas,name='estado_entradas'),
    #path('comprar-entradas/<int:id_cliente>/cancelar/',views.cancelar_compra,name='cancelar_compra'),
    #path('comprar-entradas/<int:id_cliente>/modificar/',views.modificar_compra,name='modificar_compra'),
    #path('comprar-entradas/<int:id_cliente>/',views.mostrar_compra,name='mostrar_compra'),
    
    path('',views.index,name='index'),
    path('quienes-somos/',views.quienes_somos,name='quienes_somos'),
    #con CBV
    path('comprar-entradas/',views.ComprarEntradas.as_view(),name='entradas'),
    path('comprar-entradas/estado/',views.EstadoDeEntradas.as_view(),name='estado_entradas'),
    path('comprar-entradas/<int:pk>/modificar/',views.ModificarCompra.as_view(),name='modificar_compra'),
    path('comprar-entradas/<int:pk>/cancelar/',views.CancelarCompra.as_view(),name='cancelar_compra'),
    path('comprar-entradas/<int:pk>/',views.MostrarCompra.as_view(),name='mostrar_compra'),
]

