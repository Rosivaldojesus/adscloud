from django.urls import path
from .views import index,  base, model_header, model_footer
from .views import clientes, clientesInformacoes, clienteEquipamentos

urlpatterns = [
    path('', index),
    path('clientes/', clientes),
    path('base/', base),
    path('model_header/', model_header),
    path('model_footer/', model_footer),
    path('clientesInformacoes/',clientesInformacoes),
    path('clienteEquipamentos/', clienteEquipamentos),
]