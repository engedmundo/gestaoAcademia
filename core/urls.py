from django.urls import path
# páginas de leitura
from .views import IndexView
# páginas de lista
from .views import AlunoList, PagamentoList, PlanoList, TipopagtoList
from .views import relatorio_list
# páginas de criação
from .views import AlunoCreate, PagamentoCreate, PlanoCreate, TipopagtoCreate
# páginas de atualização
from .views import AlunoUpdate, PagamentoUpdate, PlanoUpdate, TipopagtoUpdate
# páginas para deletar
from .views import AlunoDelete, PagamentoDelete, PlanoDelete, TipopagtoDelete

urlpatterns = [
   path('', IndexView.as_view(), name='index'),

   path('alunos/', AlunoList.as_view(), name='alunos'),
   path('pagamentos/', PagamentoList.as_view(), name='pagamentos'),
   path('planos/', PlanoList.as_view(), name='planos'),
   path('tipos_pagto/', TipopagtoList.as_view(), name='tipos_pagto'),
   path('relatorios/', relatorio_list, name='relatorios'),

   path('cadastro_alunos/', AlunoCreate.as_view(), name='cadastro_alunos'),
   path('cadastro_planos/', PlanoCreate.as_view(), name='cadastro_planos'),
   path('cadastro_pagamentos/', PagamentoCreate.as_view(), name='cadastro_pagamentos'),
   path('cadastro_tipopagto/', TipopagtoCreate.as_view(), name='cadastro_tipopagto'),

   path('atualiza_alunos/<int:pk>/', AlunoUpdate.as_view(), name='atualiza_alunos'),
   path('atualiza_planos/<int:pk>/', PlanoUpdate.as_view(), name='atualiza_planos'),
   path('atualiza_pagamentos/<int:pk>/', PagamentoUpdate.as_view(), name='atualiza_pagamentos'),
   path('atualiza_tipopagto/<int:pk>/', TipopagtoUpdate.as_view(), name='atualiza_tipopagto'),

   path('deleta_alunos/<int:pk>/', AlunoDelete.as_view(), name='deleta_alunos'),
   path('deleta_planos/<int:pk>/', PlanoDelete.as_view(), name='deleta_planos'),
   path('deleta_pagamentos/<int:pk>/', PagamentoDelete.as_view(), name='deleta_pagamentos'),
   path('deleta_tipopagto/<int:pk>/', TipopagtoDelete.as_view(), name='deleta_tipopagto'),
]
