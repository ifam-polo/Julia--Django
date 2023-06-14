from django.shortcuts import render
from core.models import Produto

# Create your views here.

def index(request):
    produtos = Produto.objects.all(
        
    )
    context = {
        'curso': "Programação web com django framework",
        'outro': 'django e massa',
        'produto' : 'produtos',
    }
    return render(request,'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)