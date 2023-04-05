from django.urls import path
from entradas import views

app_name = 'entradas'

urlpatterns = [
    path('hola/',views.index,name='index'),
    path('comprar-entradas/',views.sacar_entradas,name='entradas'),
]