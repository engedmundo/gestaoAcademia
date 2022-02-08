from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Aluno, Pagamento, Plano, TipoPagto
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoModelForm, PlanoModelForm, PagamentoModelForm, TipoPagtoModelForm
from django.contrib import messages
from django.urls import reverse_lazy

from django.db.models.aggregates import Sum

#=========== Listas ==================

class IndexView(TemplateView):
    template_name = 'index.html'


class AlunoList(ListView):
    model = Aluno
    template_name = 'alunos.html'
    paginate_by = 10

    def get_queryset(self):
        txt_nome = self.request.GET.get('nome')

        if txt_nome:
            alunos = Aluno.objects.filter(nome__icontains=txt_nome)
        else:
            alunos = Aluno.objects.all()

        return alunos


class PagamentoList(ListView):
    model = Pagamento
    template_name = 'pagamentos.html'
    paginate_by = 10


class PlanoList(ListView):
    model = Plano
    template_name = 'planos.html'
    paginate_by = 10


class TipopagtoList(ListView):
    model = TipoPagto
    template_name = 'tipos_pagto.html'
    paginate_by = 10

# ======== busca com filtros no banco de dados
def relatorio_list(request):
    template_name = 'relatorios.html'
    object_list = Pagamento.objects.all()

    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    if start_date and end_date:
        object_list = object_list.filter(data_pagto__range=[start_date, end_date])
        soma_dic = object_list.filter().aggregate(soma=Sum('valor_pago'))
    else:
        soma_dic = Pagamento.objects.all().aggregate(soma=Sum('valor_pago'))

    valor_soma = str(soma_dic['soma'])

    context = {
        'object_list': object_list,
        'soma': valor_soma,
        'start_date': start_date,
        'end_date': end_date,
    }

    return render(request, template_name, context)


# =========== Cadastros ===================
class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome','cpf', 'endereco', 'telefone', 'idplano']
    template_name = 'cadastro_alunos.html'
    success_url = reverse_lazy('alunos')



class PagamentoCreate(CreateView):
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'cadastro_pagamentos.html'
    success_url = reverse_lazy('pagamentos')



class PlanoCreate(CreateView):
     model = Plano
     fields = ['descricao', 'valor']
     template_name = 'cadastro_planos.html'
     success_url = reverse_lazy('planos')



class TipopagtoCreate(CreateView):
    model = TipoPagto
    fields = ['descricao']
    template_name = 'cadastro_tipopagto.html'
    success_url = reverse_lazy('tipos_pagto')


# ============== Atualizações ==================

class AlunoUpdate(UpdateView):
    model = Aluno
    fields = ['nome','cpf', 'endereco', 'telefone', 'idplano']
    template_name = 'cadastro_alunos.html'
    success_url = reverse_lazy('alunos')



class PagamentoUpdate(UpdateView):
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'cadastro_pagamentos.html'
    success_url = reverse_lazy('pagamentos')



class PlanoUpdate(UpdateView):
     model = Plano
     fields = ['descricao', 'valor']
     template_name = 'cadastro_planos.html'
     success_url = reverse_lazy('planos')



class TipopagtoUpdate(UpdateView):
    model = TipoPagto
    fields = ['descricao']
    template_name = 'cadastro_tipopagto.html'
    success_url = reverse_lazy('tipos_pagto')



# ============= DELETE ==================

class AlunoDelete(DeleteView):
    model = Aluno
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('alunos')


class PagamentoDelete(DeleteView):
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('pagamentos')



class PlanoDelete(DeleteView):
     model = Plano
     fields = ['descricao', 'valor']
     template_name = 'confirma_excluir.html'
     success_url = reverse_lazy('planos')



class TipopagtoDelete(DeleteView):
    model = TipoPagto
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('tipos_pagto')