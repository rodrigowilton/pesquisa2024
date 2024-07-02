from django.shortcuts import render

# Create your views here.
# pesquisa/views.py

from django.shortcuts import render, redirect
from .forms import PesquisaForm
from .models import Pesquisa
from openpyxl import Workbook
from django.http import HttpResponse



def export_excel(request):
    # Criar um Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Pesquisa Nilópolis - JULHO 2024"
    
    # Cabeçalhos
    headers = [
        'Data', 'Pesquisadora', 'Bairro', 'Sexo', 'Idade',
        'Voto Espontâneo', 'Voto Atual', 'Voto dos Nomes', 'Avaliação da Prefeitura'
    ]
    ws.append(headers)
    
    # Adicionar dados
    pesquisas = Pesquisa.objects.all()
    for pesquisa in pesquisas:
        ws.append([
            pesquisa.data,
            pesquisa.pesquisadora,
            pesquisa.bairro,
            pesquisa.get_sexo_display(),
            pesquisa.get_idade_display(),
            pesquisa.voto_espontaneo,
            pesquisa.get_voto_atual_display(),
            pesquisa.get_voto_dos_nomes_display(),
            pesquisa.get_avaliacao_prefeitura_display()
        ])
    
    # Criar uma resposta HTTP com o arquivo Excel
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename=pesquisa_nilopolis_julho_2024.xlsx'
    
    wb.save(response)
    return response


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


def relatorio(request):
    pesquisas = Pesquisa.objects.all()
    
    context = {
        'pesquisas': pesquisas
    }
    
    return render(request, 'relatorio.html', context)