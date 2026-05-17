from django.contrib import admin
from .models import *


class PagamentoInline(admin.TabularInline):
    model = Pagamento
    extra = 1


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'email',
        'telefone',
        'idade',
        'ativo',
        'plano',
    )

    search_fields = (
        'nome',
        'email',
        'telefone',
    )

    list_filter = (
        'ativo',
        'plano',
    )

    inlines = [PagamentoInline]


@admin.register(Plano)
class PlanoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'preco',
        'duracao_meses',
    )

    search_fields = (
        'nome',
    )


@admin.register(Instrutor)
class InstrutorAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'email',
        'especialidade',
    )

    search_fields = (
        'nome',
        'especialidade',
    )


@admin.register(Treino)
class TreinoAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
        'instrutor',
        'modalidade',
    )

    list_filter = (
        'modalidade',
    )

    search_fields = (
        'nome',
    )


@admin.register(Modalidade)
class ModalidadeAdmin(admin.ModelAdmin):

    list_display = (
        'nome',
    )


@admin.register(Pagamento)
class PagamentoAdmin(admin.ModelAdmin):

    list_display = (
        'aluno',
        'valor',
        'status',
        'data_pagamento',
    )

    list_filter = (
        'status',
    )