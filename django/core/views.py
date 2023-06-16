from django.shortcuts import render
from .models import Produto, Cliente

# Create your views here.

def index(request):

    produtos = Produto.objects.all()
    print('VIEWS: ', produtos)
        
    context = {
        '''curso': "Programação web com django framework",
        'outro': 'django e massa','''
        'produtos' : produtos,
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = {
        'produto' : prod
    }
    return render(request, 'produto.html', context)