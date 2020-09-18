from django.shortcuts import render
from .models import tbCliente


# Create your views here.
def index(request):
    return render(request, 'index.html')

def clientes(request):
    clientes = tbCliente.objects.all()
    dados = {'clientes': clientes}
    return render(request, 'clientes.html', dados)


def base(request):
    return render(request, 'base.html')

def model_header(request):
    return render(request, 'model-header.html')

def model_footer(request):
    return render(request, 'model-footer.html')
    
