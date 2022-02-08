from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Aluno, Pagamento, Plano, TipoPagto
from django.shortcuts import render, redirect, get_object_or_404
from .forms import AlunoModelForm, PlanoModelForm, PagamentoModelForm, TipoPagtoModelForm
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models.aggregates import Sum

#  =========== Listas ==================


class IndexView(TemplateView):
    template_name = 'index.html'


class AlunoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
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


class PagamentoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Pagamento
    template_name = 'pagamentos.html'
    paginate_by = 10


class PlanoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = Plano
    template_name = 'planos.html'
    paginate_by = 10


class TipopagtoList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('index')
    model = TipoPagto
    template_name = 'tipos_pagto.html'
    paginate_by = 10

# ======== busca com filtros no banco de dados


def relatorio_list(request):
    if str(request.user) != 'AnonymousUser':
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
    else:
        return redirect('index')


# =========== Cadastros ===================
class AlunoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = Aluno
    fields = ['nome', 'cpf', 'endereco', 'telefone', 'idplano']
    template_name = 'cadastro_alunos.html'
    success_url = reverse_lazy('alunos')


class PagamentoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'cadastro_pagamentos.html'
    success_url = reverse_lazy('pagamentos')


class PlanoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = Plano
    fields = ['descricao', 'valor']
    template_name = 'cadastro_planos.html'
    success_url = reverse_lazy('planos')


class TipopagtoCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('index')
    model = TipoPagto
    fields = ['descricao']
    template_name = 'cadastro_tipopagto.html'
    success_url = reverse_lazy('tipos_pagto')


# ============== Atualizações ==================

class AlunoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = Aluno
    fields = ['nome', 'cpf', 'endereco', 'telefone', 'idplano']
    template_name = 'cadastro_alunos.html'
    success_url = reverse_lazy('alunos')


class PagamentoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'cadastro_pagamentos.html'
    success_url = reverse_lazy('pagamentos')


class PlanoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = Plano
    fields = ['descricao', 'valor']
    template_name = 'cadastro_planos.html'
    success_url = reverse_lazy('planos')


class TipopagtoUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('index')
    model = TipoPagto
    fields = ['descricao']
    template_name = 'cadastro_tipopagto.html'
    success_url = reverse_lazy('tipos_pagto')


# ============= DELETE ==================

class AlunoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('index')
    model = Aluno
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('alunos')


class PagamentoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('index')
    model = Pagamento
    fields = ['valido_de', 'valido_ate', 'data_pagto', 'valor_pago', 'tipo_pagto', 'aluno']
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('pagamentos')


class PlanoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('index')
    model = Plano
    fields = ['descricao', 'valor']
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('planos')


class TipopagtoDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('index')
    model = TipoPagto
    template_name = 'confirma_excluir.html'
    success_url = reverse_lazy('tipos_pagto')
