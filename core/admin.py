from django.contrib import admin
from .models import Plano, Aluno, TipoPagto, Pagamento

# Register your models here.


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):
    list_display = ('descricao', 'valor')


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'endereco', 'telefone')


@admin.register(TipoPagto)
class TipoPagtoAdmin(admin.ModelAdmin):
    list_display = ('descricao', )


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):
    list_display = ('aluno', 'valor_pago', 'valido_de', 'valido_ate', 'data_pagto', )
