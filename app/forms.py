from django import forms
from .models import Aluno, Plano, Pagamento, Treino

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = '__all__'

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'preco', 'duracao_meses', 'descricao']

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['aluno', 'valor', 'data_pagamento', 'status']

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'descricao', 'instrutor', 'modalidade']