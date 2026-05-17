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

    def __str__(self):
        return self.nome

