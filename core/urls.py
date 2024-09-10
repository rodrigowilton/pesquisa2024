# pesquisa/urls.py

from django.urls import path
from .views import pesquisa_view, sucesso_view

urlpatterns = [
    path('', pesquisa_view, name='pesquisa'),  # Define a URL base como a view de pesquisa
    path('sucesso/', sucesso_view, name='sucesso'),
]
