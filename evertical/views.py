from django.shortcuts import render, get_object_or_404
from .models import tbCliente, tbEquipamento,tbArtigos, tbManuais, tbPreventivas, tbSenhasPadroes, tbWework
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q


# Create your views here.
def index(request):

    artigo = tbArtigos.objects.all().order_by('-id')[:3]

    return render(request, 'index.html', {'artigo': artigo})

def artigos(request):
    artigos = tbArtigos.objects.all()
    queryset = request.GET.get('q')
    if queryset:
        artigos = tbArtigos.objects.filter(
            Q(artigoTitulo__icontains=queryset)|
            Q(artigoSubtitulo__icontains=queryset)|
            Q(artigoTexto__icontains=queryset)
        )
    dados = {'artigos': artigos}
    return render(request, 'artigos.html', dados)

def artigoVisualizacao(request):
    artigo = request.GET.get('id')
    if artigo:
        artigo = tbArtigos.objects.get(id=artigo)
        return render(request,'artigoVisualizacao.html', {'artigo':artigo})

def clientes(request):
    clientes = tbCliente.objects.filter().order_by('clienteNome')
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

def dashboard(request):
    # Faz a contagam de equipamentos cadastrados por sistemas
    qnt_equi_cftv = tbEquipamento.objects.filter(equipamentoSistema = 2).count()
    qnt_equi_sai = tbEquipamento.objects.filter(equipamentoSistema=3).count()
    qnt_equi_sca = tbEquipamento.objects.filter(equipamentoSistema=4).count()
    qnt_equi_sap = tbEquipamento.objects.filter(equipamentoSistema=5).count()
    qnt_equi_sdai = tbEquipamento.objects.filter(equipamentoSistema=6).count()


    return render(request, 'dashboard.html',{

                                            'qnt_equi_cftv':qnt_equi_cftv,
                                             'qnt_equi_sai':qnt_equi_sai,
                                              'qnt_equi_sca':qnt_equi_sca,
                                               'qnt_equi_sap':qnt_equi_sap,
                                                'qnt_equi_sdai':qnt_equi_sdai,

                                                 })


def manuaisFabricantes(request):
    manualFabricante = tbManuais.objects.all().order_by('manualFabricante')
    queryset = request.GET.get('q')
    if queryset:
        manualFabricante = tbManuais.objects.filter(
            Q(manualNome__icontains=queryset) |
            Q(manualDescricao__icontains=queryset) |
            Q(manualFabricante__icontains=queryset)
        )
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

def wework(request):
    wework = tbWework.objects.all()
    return render(request, 'wework.html', {'wework':wework})

def weworkView(request):
    wework = request.GET.get('id')
    dados = {}
    if wework:
        dados['wework'] = tbWework.objects.get(id=wework)
    return render(request, 'weworkView.html', dados)

def base(request):
    return render(request, 'base.html')

def model_header(request):
    return render(request, 'model-header.html')

def model_footer(request):
    return render(request, 'model-footer.html')
    
