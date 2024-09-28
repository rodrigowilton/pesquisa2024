from django.shortcuts import render

# Create your views here.
# pesquisa/views.py

from django.shortcuts import render, redirect
from .forms import PesquisaForm
from .models import Pesquisa
from openpyxl import Workbook
from django.http import HttpResponse
from django.contrib import messages
import pandas as pd

"""
def importar_dados(request):
    if request.method == 'POST' and request.FILES['arquivo']:
        arquivo = request.FILES['arquivo']
        if arquivo.name.endswith('.csv'):
            df = pd.read_csv(arquivo)
        elif arquivo.name.endswith('.xlsx'):
            df = pd.read_excel(arquivo)
        else:
            messages.error(request, 'Formato de arquivo não suportado.')
            return redirect('importar_dados')
        
        # Verificar colunas
        required_columns = ['Data', 'Pesquisadora', 'Bairro', 'Questao1', 'Questao2', 'Questao3', 'Questao4',
                            'Questao5']
        missing_columns = [col for col in required_columns if col not in df.columns]
        
        if missing_columns:
            messages.error(request, f'As seguintes colunas estão faltando: {", ".join(missing_columns)}')
            return redirect('importar_dados')
        
        # Mapeando valores das questões para o modelo
        sexo_mapping = {
            'MASCULINO': 'M',
            'FEMININO': 'F',
        }
        
        idade_mapping = {
            '16 A 25 ANOS': '16_25',
            '26 A 34 ANOS': '26_34',
            '35 A 55 ANOS': '35_55',
            'ACIMA DE 55 ANOS': 'acima_55',
        }
        
        voto_atual_mapping = {
            'ABRAAZINHO': 'abraazinho',
            'ROGERIO RIBEIRO': 'rogerio_ribeiro',
            'NÃO SABE': 'nao_sabe',
        }
        
        avaliacao_mapping = {
            'REGULAR': 'regular',
            'BOM': 'bom',
            'RUIM': 'ruim',
            'PÉSSIMO': 'pessimo',
        }
        
        for _, row in df.iterrows():
            try:
                pesquisa = Pesquisa(
                    data=row['Data'],
                    pesquisadora=row['Pesquisadora'],
                    bairro=row['Bairro'],
                    sexo=sexo_mapping.get(row['Questao1'].strip(), ''),  # Mapear sexo
                    idade=idade_mapping.get(row['Questao2'].strip(), ''),  # Mapear idade
                    voto_espontaneo=row['Questao3'],  # Voto espontâneo
                    voto_atual=voto_atual_mapping.get(row['Questao4'].strip(), ''),  # Mapear voto atual
                    avaliacao_prefeitura=avaliacao_mapping.get(row['Questao5'].strip(), ''),
                    # Mapear avaliação da prefeitura
                )
                pesquisa.full_clean()  # Valida antes de salvar
                pesquisa.save()
            except Exception as e:
                messages.error(request, f'Erro ao importar linha: {e}')
                continue
        
        messages.success(request, 'Dados importados com sucesso!')
        return redirect('importar_dados')
    
    # Para requisições GET, sempre retornar o formulário de importação
    return render(request, 'importar_dados.html')
"""

def export_excel(request):
    # Criar um Workbook
    wb = Workbook()
    ws = wb.active
    ws.title = "Pesquisa Nilópolis - JULHO 2024"
    
    # Cabeçalhos
    headers = [
        'Data', 'Pesquisadora', 'Bairro', 'Sexo', 'Idade',
        'Voto Espontâneo', 'Voto Atual', 'Avaliação da Prefeitura'
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