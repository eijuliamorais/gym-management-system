from django.db import models

# Create your models here.
class Plano(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    duracao_meses = models.IntegerField()
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Instrutor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    especialidade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Modalidade(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()

    def __str__(self):
        return self.nome

class Treino(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    instrutor = models.ForeignKey(
        Instrutor,
        on_delete=models.CASCADE
    )
    modalidade = models.ForeignKey(
        Modalidade,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.nome


class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=20)
    idade = models.IntegerField()
    ativo = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    plano = models.ForeignKey(
        Plano,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    treino = models.ForeignKey(
        Treino,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.nome

class Pagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    valor = models.DecimalField(
        max_digits=8, decimal_places=2,
        null=True, blank=True,   # <-- agora pode ficar vazio
        help_text="Deixe em branco para usar o preço do plano do aluno."
    )
    data_pagamento = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('PAGO', 'Pago'),
            ('PENDENTE', 'Pendente'),
            ('ATRASADO', 'Atrasado'),
        ]
    )

    def save(self, *args, **kwargs):
        # Se o valor não foi informado e o aluno tem um plano, preenche com o preço do plano
        if self.valor is None and self.aluno and self.aluno.plano:
            self.valor = self.aluno.plano.preco
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.aluno.nome} - {self.status}"