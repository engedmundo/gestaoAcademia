from django.db import models


# Create your models here.
class Plano(models.Model):
    descricao = models.CharField('Descrição', max_length=30)
    valor = models.DecimalField('Valor Plano', max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'

    def __str__(self):
        return self.descricao


class Aluno(models.Model):
    nome = models.CharField('Nome do Aluno', max_length=50)
    cpf = models.CharField('CPF', null=True, blank=True, max_length=11)
    endereco = models.CharField('Endereço', null=True, blank=True, max_length=50)
    telefone = models.CharField('Telefone', null=True, blank=True, max_length=15)
    idplano = models.ForeignKey('core.Plano', verbose_name='Plano', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return self.nome


class TipoPagto(models.Model):
    descricao = models.CharField('Descrição do pagamento', max_length=50)

    class Meta:
        verbose_name = 'Tipo de pagamento'
        verbose_name_plural = 'Tipos de pagamento'

    def __str__(self):
        return self.descricao


class Pagamento(models.Model):
    aluno = models.ForeignKey('Aluno', verbose_name='Aluno', on_delete=models.CASCADE)
    valido_de = models.DateField('Válido de:', max_length=50)
    valido_ate = models.DateField('Válido até:', max_length=50)
    data_pagto = models.DateField('Data do pagamento', max_length=50)
    valor_pago = models.DecimalField('Valor Pago', max_digits=8, decimal_places=2, max_length=50)
    tipo_pagto = models.ForeignKey('TipoPagto', verbose_name='Tipo Pagamento', on_delete=models.CASCADE)


    class Meta:
        verbose_name = 'Pagamento'
        verbose_name_plural = 'Pagamentos'

