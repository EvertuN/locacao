from django.core.validators import RegexValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User, Group


class TipoVeiculo(models.Model):
    codigo = models.CharField(max_length=3)
    nome = models.CharField(max_length=200)
    ar_condicionado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Tipo de Veículo'
        verbose_name_plural = 'Tipos de Veículos'
        # ordering = ['-publicado']

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    numero = models.AutoField(primary_key=True)
    data_proxima_manutencao = models.DateField(verbose_name="Próxima Manutenção")
    placa = models.CharField(max_length=7, verbose_name="Placa")
    tipo_veiculo = models.ForeignKey(TipoVeiculo, on_delete=models.CASCADE, null=True, blank=True)

    """class Meta:
        verbose_name = 'Veiculo'
        verbose_name_plural = 'Veiculos'
        # ordering = ['-publicado']
    """

    def __str__(self):
        return f"{self.tipo_veiculo.nome} - {self.placa}" if self.tipo_veiculo else f"Veiculo - {self.placa}"


"""class Onibus(models.Model):
    veiculo = models.OneToOneField(Veiculo, on_delete=models.CASCADE, primary_key=True)
    num_passageiros = models.IntegerField(verbose_name="Número de Passageiros")
    leito = models.BooleanField(default=False)
    sanitario = models.BooleanField(default=False, verbose_name="Sanitário")

    #class Meta:
    #    verbose_name = 'Ônibus'
    #    verbose_name_plural = 'Ônibus'
    #    # ordering = ['-publicado']
    

    def __str__(self):
        return f"Ônibus - {self.num_passageiros} passageiros"

    def get_tipo(self):
        return f"Ônibus - {self.num_passageiros} passageiros"
"""


class Contrato(models.Model):
    numero = models.AutoField(primary_key=True)
    data = models.DateField(verbose_name="Data da Locação")
    duracao = models.IntegerField(verbose_name="Duração do contrato(Em dias)")
    cliente = models.ForeignKey('Cliente', on_delete=models.CASCADE)
    veiculo = models.ForeignKey('Veiculo', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Contrato'
        verbose_name_plural = 'Contratos'
        # ordering = ['-publicado']

    def __str__(self):
        return f'{self.numero} - {self.cliente.nome}'


class Cliente(models.Model):
    num_hab = models.AutoField(primary_key=True)
    estado_hab = models.CharField(max_length=25, verbose_name="Estado da Habilitação")
    nome = models.CharField(max_length=100, verbose_name="Nome Completo")
    end = models.CharField(max_length=255, verbose_name="Endereço")
    telefone = models.CharField(max_length=11)

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        # ordering = ['-publicado']

    def __str__(self):
        return self.nome
