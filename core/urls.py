from django.urls import path
from .views import index, ClienteCadastroView

urlpatterns = [
    path('', index, name='index'),
    path('clientes/cadastrar/', ClienteCadastroView.as_view(), name='clientes_cadastro'),
    #path('automoveis/cadastrar/', AutomoveisCadastroView.as_view(), name='automoveis_cadastro'),
    #path('contratos/cadastrar/', ContratosCadastroView.as_view(), name='contratos_cadastro'),
    #path('tiposveiculos/cadastrar/', TiposVeiculosCadastroView.as_view(), name='tipos_veiculos_cadastro'),
    #path('veiculos/cadastrar/', VeiculosCadastroView.as_view(), name='veiculos_cadastro'),
    #path('onibus/cadastrar/', OnibusCadastroView.as_view(), name='onibus_cadastro'),
]