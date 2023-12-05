from django.contrib import admin
from .models import TipoVeiculo, Veiculo, Automovel, Onibus, Contrato, Cliente

admin.site.register(TipoVeiculo)
admin.site.register(Veiculo)
admin.site.register(Automovel)
admin.site.register(Onibus)
admin.site.register(Contrato)
admin.site.register(Cliente)

