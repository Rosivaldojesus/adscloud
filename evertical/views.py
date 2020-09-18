from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')

def clientes(request):
    return render(request, 'clientes.html')


def base(request):
    return render(request, 'base,html')

def model_header(request):
    return render(request, 'model-header.html')

def model_footer(request):
    return render(request, 'model-footer.html')
    
