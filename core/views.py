from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import ClienteForm, ContratoForm, TipoVeiculoForm, VeiculoForm
from django.views import View


def index(request):
    return render(request, 'index.html')


def specialuser(user):
    return user.groups.filter(name='especiais').exists()


@user_passes_test(specialuser)
def contrato_view(request):
    pass


class IndexView(View):
    template_name = 'index.html'


class ClienteCadastroView(View):
    template_name = 'cliente_form.html'

    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('admin:core_cliente_changelist')
        else:
            messages.error(request, 'Não foi possível cadastrar o cliente.')
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
        return render(request, self.template_name, {'form': form})


class ContratoCadastroView(View):
    template_name = 'contrato_form.html'

    def get(self, request, *args, **kwargs):
        form = ContratoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato cadastrado com sucesso!')
            return redirect('admin:core_contrato_changelist')
        else:
            messages.error(request, 'Não foi possível cadastrar o contrato.')
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
        return render(request, self.template_name, {'form': form})


class TiposVeiculosCadastroView(View):
    template_name = 'tipo_veiculo.html'

    def get(self, request, *args, **kwargs):
        form = TipoVeiculoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = TipoVeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contrato cadastrado com sucesso!')
            return redirect('admin:core_tipoveiculo_changelist')
        else:
            messages.error(request, 'Não foi possível cadastrar o contrato.')
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
        return render(request, self.template_name, {'form': form})


class VeiculosCadastroView(View):
    template_name = 'veiculo.html'

    def get(self, request, *args, **kwargs):
        form = VeiculoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veiculo cadastrado com sucesso!')
            return redirect('admin:core_veiculo_changelist')
        else:
            messages.error(request, 'Não foi possível cadastrar o cliente.')
            for field, errors in form.errors.items():
                messages.error(request, f"{field}: {', '.join(errors)}")
        return render(request, self.template_name, {'form': form})
