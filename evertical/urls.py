from django.urls import path
from .views import index,  base, model_header, model_footer
from .views import artigos, artigoVisualizacao
from .views import clientes, clientesInformacoes, clienteEquipamentos, clienteEquipamentosInformacoes
from .views import manuaisFabricantes, manuaisPreventivas, manuaisPreventivasInformacoes
from .views import senhasPadroes
from .views import wework, weworkView
from .views import dashboard

urlpatterns = [
    path('', index),
    path('clientes/', clientes),
    path('base/', base),
    path('model_header/', model_header),
    path('model_footer/', model_footer),
    path('clientesInformacoes/',clientesInformacoes),
    path('clienteEquipamentos/', clienteEquipamentos),
    path('clienteEquipamentosInformacoes/',clienteEquipamentosInformacoes),
    path('artigos/', artigos),
    path('artigoVisualizacao/', artigoVisualizacao),

    path('dashboard/', dashboard),


    path('manuaisFabricantes/', manuaisFabricantes),
    path('manuaisPreventivas/', manuaisPreventivas),
    path('manuaisPreventivasInformacoes/',manuaisPreventivasInformacoes),

    path('senhasPadroes/', senhasPadroes),

    path('wework/', wework),
    path('weworkView/', weworkView),
]