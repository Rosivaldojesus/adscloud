from django.urls import path
from .views import index,  base, model_header, model_footer
from .views import artigos, artigoVisualizacao
from .views import clientes, clientesInformacoes, clienteEquipamentos, clienteEquipamentosInformacoes
from .views import manuaisFabricantes, manuaisPreventivas, manuaisPreventivasInformacoes, manuais, fabricantes
from .views import senhasPadroes, brBanner
from .views import wework, weworkView, weworkUpdate
from .views import dashboard
from .views import scirp

urlpatterns = [
    path('brBanner/', brBanner),

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

    path('manuais/', manuais),
    path('fabricantes/', fabricantes),


    path('manuaisFabricantes/', manuaisFabricantes),
    path('manuaisPreventivas/', manuaisPreventivas),
    path('manuaisPreventivasInformacoes/',manuaisPreventivasInformacoes),

    path('senhasPadroes/', senhasPadroes),

    path('wework/', wework),
    path('weworkUpdate/<int:id>', weworkUpdate),
    path('weworkView/', weworkView),


    path('scirp/', scirp),

]