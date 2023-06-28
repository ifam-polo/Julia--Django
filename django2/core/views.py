from django.shortcuts import render, redirect
from .forms import ContatoForm, ProdutoModelForm
from django.contrib import messages
from .models import Produto

def index(request):
    context = {
        'produtos':Produto.objects.all()
    }
    return render(request, 'index.html')

def produto(request):

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "Salvo com sucesso")
                form = ProdutoModelForm()
            else:
                messages.error(request, "Erro ao salvar produto")
        else: 
            form = ProdutoModelForm()
        context = {
            'form': form
        }
        return render(request, 'produto.html', context)
    else:
        return redirect('index')
def contato(request):
    form = ContatoForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'E-mail enviado com sucesso')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar email')
    
    context = {
        'form': form
    }
    
    return render(request, 'contato.html', context)
