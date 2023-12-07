from django.contrib import admin
from django import forms
from .models import TipoVeiculo, Veiculo, Contrato, Cliente


class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tipo_veiculo'].widget = (
            forms.widgets.Select(choices=[(tipo.id, tipo.nome) for tipo in TipoVeiculo.objects.all()]))


"""class AutomovelInline(admin.StackedInline):
    model = Automovel
    can_delete = False"""


"""class OnibusInline(admin.StackedInline):
    model = Onibus
    can_delete = False"""


class VeiculoAdmin(admin.ModelAdmin):
    form = VeiculoForm
    list_display = ['numero', 'placa', 'tipo_veiculo']

    def save_model(self, request, obj, form, change):
        tipo_veiculo_id = request.POST.get('tipo_veiculo')
        tipo_veiculo = None

        if tipo_veiculo_id:
            tipo_veiculo = TipoVeiculo.objects.get(pk=tipo_veiculo_id)
            obj.tipo_veiculo = tipo_veiculo

        obj.save()

        if tipo_veiculo and tipo_veiculo.nome == 'automovel':
            automovel, created = Automovel.objects.get_or_create(veiculo=obj)
            if created:
                automovel.num_portas = 4
                automovel.save()
        elif tipo_veiculo and tipo_veiculo.nome == 'onibus':
            onibus, created = Onibus.objects.get_or_create(veiculo=obj)
            if created:
                onibus.num_passageiros = 50
                onibus.save()


admin.site.register(TipoVeiculo)
admin.site.register(Veiculo, VeiculoAdmin)
#admin.site.register(Automovel)
#admin.site.register(Onibus)
admin.site.register(Contrato)
admin.site.register(Cliente)
