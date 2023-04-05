from django.urls import path
from entradas import views

app_name = 'entradas'

urlpatterns = [
    path('',views.index,name='index'),
]