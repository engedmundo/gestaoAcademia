from django import forms
from .models import Aluno, Pagamento, Plano, TipoPagto


class AlunoModelForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'endereco', 'telefone', 'idplano']


class PlanoModelForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['descricao', 'valor']


class TipoPagtoModelForm(forms.ModelForm):
    class Meta:
        model = TipoPagto
        fields = ['descricao', ]


class PagamentoModelForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['aluno', 'valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', ]

