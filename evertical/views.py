from django.shortcuts import render
from .models import tbCliente, tbEquipamento,tbArtigos, tbManuais, tbPreventivas, tbSenhasPadroes
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404




# Create your views here.
def index(request):
    return render(request, 'index.html')

def artigos(request):
    artigos = tbArtigos.objects.all()
    dados = {'artigos': artigos}
    return render(request, 'artigos.html', dados)

def artigoVisualizacao(request):
    artigo = request.GET.get('id')
    if artigo:
        artigo = tbArtigos.objects.get(id=artigo)
        return render(request,'artigoVisualizacao.html', {'artigo':artigo})

def clientes(request):
    clientes = tbCliente.objects.all()
    dados = {'clientes': clientes}
    return render(request, 'clientes.html', dados)

def clientesInformacoes(request):
    cliente = request.GET.get('id')
    dados = {}
    if cliente:
        dados['cliente'] = tbCliente.objects.get(id=cliente)
    return render(request, 'clientesInformacoes.html', dados)

def clienteEquipamentos(request):
    equipamento = request.GET.get('id')
    dados = {}
    if equipamento:
        dados['equipamento'] = tbEquipamento.objects.filter(equipamentoCliente=equipamento)
    return render(request, 'clienteEquipamentos.html', dados)

def clienteEquipamentosInformacoes(request):
    equipamento = request.GET.get('id')
    if equipamento:
        equipamento = tbEquipamento.objects.get(id=equipamento)
    return render(request, 'clienteEquipamentosInformacoes.html', {'equipamento':equipamento})

def manuaisFabricantes(request):
    manualFabricante = tbManuais.objects.all()
    return render(request, 'manuaisFabricantes.html',{'manualFabricante':manualFabricante})

def manuaisPreventivas(request):
    manualPreventiva = tbPreventivas.objects.all()
    return render(request, 'manuaisPreventivas.html', {'manualPreventiva':manualPreventiva})

def manuaisPreventivasInformacoes(request):
    preventiva = request.GET.get('id')
    dados = {}
    if preventiva:
        dados['preventiva'] = tbPreventivas.objects.get(id=preventiva)
    return render(request, 'manuaisPreventivasInformacoes.html', dados)

def senhasPadroes(request):
    senha = tbSenhasPadroes.objects.all()
    return render(request, 'senhasPadroes.html', {'senha':senha})


def base(request):
    return render(request, 'base.html')

def model_header(request):
    return render(request, 'model-header.html')

def model_footer(request):
    return render(request, 'model-footer.html')
    
