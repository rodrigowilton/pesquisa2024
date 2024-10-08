# Generated by Django 5.1.1 on 2024-09-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='bairro',
            field=models.CharField(choices=[('CABRAL', 'CABRAL'), ('CABUIS', 'CABUIS'), ('CENTRO', 'CENTRO'), ('NOSSA Sra. FATIMA', 'NOSSA Sra. FATIMA'), ('NOVA CIDADE', 'NOVA CIDADE'), ('NOVO HORIZONTE', 'NOVO HORIZONTE'), ('OLINDA', 'OLINDA'), ('PAIOL', 'PAIOL')], max_length=100),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='pesquisadora',
            field=models.CharField(choices=[('Karina', 'Karina'), ('Kamila', 'Kamila'), ('Raquel', 'Raquel'), ('Rogerio', 'Rogerio')], max_length=100),
        ),
    ]
