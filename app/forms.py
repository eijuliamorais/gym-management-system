from django import forms
from .models import Aluno, Plano, Pagamento, Treino

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do aluno'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }),

            'telefone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': '(00) 00000-0000'
            }),

            'idade': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Idade'
            }),

            'ativo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            }),
        }

class PlanoForm(forms.ModelForm):
    class Meta:
        model = Plano
        fields = ['nome', 'preco', 'duracao_meses', 'descricao']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do plano'
            }),

            'preco': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Valor do plano'
            }),

            'duracao_meses': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Duração em meses'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição do plano'
            }),
        }

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['aluno', 'valor', 'data_pagamento', 'status']

        widgets = {
            'aluno': forms.Select(attrs={
                'class': 'form-select'
            }),

            'valor': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o valor do pagamento'
            }),

            'data_pagamento': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),

            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
        }

class TreinoForm(forms.ModelForm):
    class Meta:
        model = Treino
        fields = ['nome', 'descricao', 'instrutor', 'modalidade']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do treino'
            }),

            'descricao': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Descrição do treino'
            }),

            'instrutor': forms.Select(attrs={
                'class': 'form-select'
            }),

            'modalidade': forms.Select(attrs={
                'class': 'form-select'
            }),
        }