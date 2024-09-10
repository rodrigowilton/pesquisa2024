from django.shortcuts import render

# Create your views here.
# pesquisa/views.py

from django.shortcuts import render, redirect
from .forms import PesquisaForm

def pesquisa_view(request):
    if request.method == 'POST':
        form = PesquisaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = PesquisaForm()
    return render(request, 'pesquisa_form.html', {'form': form})

def sucesso_view(request):
    return render(request, 'sucesso.html')
