# pesquisa/urls.py

from django.urls import path

from . import views
from .views import pesquisa_view, sucesso_view
from .views import relatorio
from .views import relatorio, export_excel, importar_dados



urlpatterns = [
    path('', pesquisa_view, name='pesquisa'),  # Define a URL base como a view de pesquisa
    path('sucesso/', sucesso_view, name='sucesso'),
    path('relatorio/', relatorio, name='relatorio'),
    path('export_excel/', export_excel, name='export_excel'),
    path('importar/', views.importar_dados, name='importar_dados'),

]
