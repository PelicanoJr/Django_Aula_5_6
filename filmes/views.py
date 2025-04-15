from django.shortcuts import render, redirect
from filmes.models import Filme
from filmes.forms import FilmeForm

def filmes_view(request): 
    filmes = Filme.objects.all().order_by('titulo') # se inluir -titulo, a ordenação será decrescente
    search = request.GET.get('search')
    if search:  
        filmes = Filme.objects.filter(titulo__contains=search)  # se usar o icontains, a busca não será case sensitive
        
    return render(request, 'filmes.html' , {'filmes': filmes}) 

def novo_filmes_view(request):
    if request.method == 'POST':
        novo_filme_form = FilmeForm(request.POST, request.FILES)    
        if novo_filme_form.is_valid():
            novo_filme_form.save()   
            return redirect('filmes_list')  
    else:
        novo_filme_form = FilmeForm()
    return render(request, 'novo_filme.html', {'novo_filme_form': novo_filme_form})

