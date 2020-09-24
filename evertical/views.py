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
    # Quantidade de administradora
    qnt_bbz = tbCliente.objects.filter(clienteAdministradora= 1).count()
    qnt_cbre = tbCliente.objects.filter(clienteAdministradora=2).count()
    qnt_carrefour = tbCliente.objects.filter(clienteAdministradora=3).count()
    qnt_pina = tbCliente.objects.filter(clienteAdministradora=4).count()
    qnt_ccp = tbCliente.objects.filter(clienteAdministradora=5).count()
    qnt_saphyr = tbCliente.objects.filter(clienteAdministradora=6).count()
    qnt_iguatemi = tbCliente.objects.filter(clienteAdministradora=7).count()
    # Quantidade de equipamento por cliente
    atrium_VII = tbEquipamento.objects.filter(equipamentoCliente=1).count()
    birmann31 = tbEquipamento.objects.filter(equipamentoCliente=2).count()
    capitalCenter = tbEquipamento.objects.filter(equipamentoCliente=3).count()
    eTower = tbEquipamento.objects.filter(equipamentoCliente=4).count()
    eenu = tbEquipamento.objects.filter(equipamentoCliente=5).count()
    hlFariaLima = tbEquipamento.objects.filter(equipamentoCliente=6).count()
    jk360 = tbEquipamento.objects.filter(equipamentoCliente=7).count()
    jardimPamplonaShopping = tbEquipamento.objects.filter(equipamentoCliente=8).count()
    morumbiPlaza = tbEquipamento.objects.filter(equipamentoCliente=9).count()
    paulista1100 = tbEquipamento.objects.filter(equipamentoCliente=10).count()
    pinacoteca = tbEquipamento.objects.filter(equipamentoCliente=11).count()
    shoppingGrandPlaza = tbEquipamento.objects.filter(equipamentoCliente=11).count()
    shoppingGranjaVianna = tbEquipamento.objects.filter(equipamentoCliente=12).count()
    shoppingIguatemiAlphaville = tbEquipamento.objects.filter(equipamentoCliente=13).count()
    skyCorporate = tbEquipamento.objects.filter(equipamentoCliente=14).count()
    vistaFariaLima = tbEquipamento.objects.filter(equipamentoCliente=15).count()
    workBelaCintra = tbEquipamento.objects.filter(equipamentoCliente=16).count()
    iguatemiAlphaville = tbEquipamento.objects.filter(equipamentoCliente=17).count()


    return render(request, 'dashboard.html',{
                                            # Quantidade de manuais cadastrados
                                            'qnt_equi_cftv':qnt_equi_cftv,
                                             'qnt_equi_sai':qnt_equi_sai,
                                              'qnt_equi_sca':qnt_equi_sca,
                                               'qnt_equi_sap':qnt_equi_sap,
                                                'qnt_equi_sdai':qnt_equi_sdai,
                                            # Quantidade de administradora
                                            'qnt_bbz': qnt_bbz,
                                             'qnt_cbre': qnt_cbre,
                                              'qnt_carrefour': qnt_carrefour,
                                               'qnt_pina': qnt_pina,
                                                 'qnt_ccp': qnt_ccp,
                                                  'qnt_saphyr': qnt_saphyr,
                                                   'qnt_iguatemi':qnt_iguatemi,
                                            # Quantidade de administradora
                                            # Quantidade de equipmantos por cliente
                                            'atrium_VII': atrium_VII,
                                            'birmann31': birmann31,
                                            'capitalCenter': capitalCenter,
                                            'eTower': eTower,
                                            'eenu': eenu,
                                            'hlFariaLima': hlFariaLima,
                                            'morumbiPlaza': morumbiPlaza,
                                            'jardimPamplonaShopping': jardimPamplonaShopping,
                                            'jk360': jk360,
                                            'paulista1100': paulista1100,
                                            'pinacoteca': pinacoteca,
                                            'shoppingGrandPlaza': shoppingGrandPlaza,
                                            'shoppingGranjaVianna': shoppingGranjaVianna,
                                            'skyCorporate': skyCorporate,
                                            'workBelaCintra': workBelaCintra,
                                            'vistaFariaLima': vistaFariaLima,
                                            'shoppingIguatemiAlphaville': shoppingIguatemiAlphaville,

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
    queryset = request.GET.get('')
    if queryset:
        manualPreventiva =  tbPreventivas.objects.filter(
            Q(preventivaEquipamento__icontains=queryset) |
            Q(manualSistema__icontains=queryset) |
            Q(preventivaProcedimento__icontains=queryset)
        )
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
    
