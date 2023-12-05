from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render, redirect
from .forms import ClienteForm
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


"""
class ClienteCadastroView(View):
    template_name = 'cliente_form.html'

    def get(self, request, *args, **kwargs):
        form = ClienteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes_cadastro')
        return render(request, self.template_name, {'form': form})
"""


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
