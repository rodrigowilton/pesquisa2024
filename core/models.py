from django.db import models


class Pesquisa(models.Model):
	SEXO_CHOICES = [
		('M', 'MASCULINO'),
		('F', 'FEMININO'),
	]
	
	IDADE_CHOICES = [
		('16_25', '16 A 25 ANOS'),
		('26_34', '26 A 34 ANOS'),
		('35_55', '35 A 55 ANOS'),
		('acima_55', 'ACIMA DE 55 ANOS'),
	]
	
	PREFEITO_CHOICES = [
		('abraazinho', 'ABRAAZINHO'),
		('rogerio_ribeiro', 'ROGERIO RIBEIRO'),
		('nao_sabe', 'NÃO SABE'),
	]
	
	PREFEITO_DOS_NOMES_CHOICES = [
		('abraazinho', 'ABRAAZINHO'),
		('rogerio_ribeiro', 'ROGERIO RIBEIRO'),
		('dedinho', 'DEDINHO'),
		('sergio_sessim', 'SERGIO SESSIM'),
		('rafael_nobre', 'RAFAEL NOBRE'),
		('neca', 'NECA'),
		('alessandro_calazans', 'ALESSANDRO CALAZANS'),
		('nao_sabe', 'Não Sabe'),
	]
	
	AVALIACAO_CHOICES = [
		('bom', 'BOM'),
		('regular', 'REGULAR'),
		('ruim', 'RUIM'),
		('pessimo', 'PÉSSIMO'),
	]
	
	BAIRRO_CHOICES = [
		('CABRAL', 'CABRAL'),
		('CABUIS', 'CABUIS'),
		('CENTRO', 'CENTRO'),
		('NOSSA Sra. FATIMA', 'NOSSA Sra. FATIMA'),
		('NOVA CIDADE', 'NOVA CIDADE'),
		('NOVO HORIZONTE', 'NOVO HORIZONTE'),
		('OLINDA', 'OLINDA'),
		('PAIOL', 'PAIOL'),
	]
	
	PESQUISADORA_CHOICES = [
		('Karina', 'Karina'),
		('Kamila', 'Kamila'),
		('Raquel', 'Raquel'),
		('Rogerio', 'Rogerio'),
	]
	
	data = models.DateField()
	pesquisadora = models.CharField(max_length=100, choices=PESQUISADORA_CHOICES)
	bairro = models.CharField(max_length=100, choices=BAIRRO_CHOICES)
	
	sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
	idade = models.CharField(max_length=10, choices=IDADE_CHOICES)
	voto_espontaneo = models.CharField(max_length=100, blank=True)
	voto_atual = models.CharField(max_length=20, choices=PREFEITO_CHOICES)
	voto_dos_nomes = models.CharField(max_length=50, choices=PREFEITO_DOS_NOMES_CHOICES)
	avaliacao_prefeitura = models.CharField(max_length=10, choices=AVALIACAO_CHOICES)
	
	def __str__(self):
		return f"Pesquisa {self.data} - {self.pesquisadora}"
