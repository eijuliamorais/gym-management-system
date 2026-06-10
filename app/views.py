from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Aluno, Plano, Pagamento, Treino
from .forms import AlunoForm, PlanoForm, PagamentoForm, TreinoForm

# HOME 
@login_required
def home(request):
    total_alunos = Aluno.objects.count()
    total_planos = Plano.objects.count()
    total_pagamentos = Pagamento.objects.count()
    contexto = {
        'total_alunos': total_alunos,
        'total_planos': total_planos,
        'total_pagamentos': total_pagamentos,
    }
    return render(request, 'home.html', contexto)

# ALUNOS 
@login_required
def listar_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'alunos/listar.html', {'alunos': alunos})

@login_required
def criar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm()
    return render(request, 'alunos/form.html', {'form': form})

@login_required
def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('listar_alunos')
    else:
        form = AlunoForm(instance=aluno)
    return render(request, 'alunos/form.html', {'form': form})

@login_required
def excluir_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        aluno.delete()
        return redirect('listar_alunos')
    return render(request, 'alunos/excluir.html', {'aluno': aluno})

# PLANOS 
@login_required
def listar_planos(request):
    planos = Plano.objects.all()
    return render(request, 'planos/listar.html', {'planos': planos})

@login_required
def criar_plano(request):
    if request.method == 'POST':
        form = PlanoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_planos')
    else:
        form = PlanoForm()
    return render(request, 'planos/form.html', {'form': form})

@login_required
def editar_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    if request.method == 'POST':
        form = PlanoForm(request.POST, instance=plano)
        if form.is_valid():
            form.save()
            return redirect('listar_planos')
    else:
        form = PlanoForm(instance=plano)
    return render(request, 'planos/form.html', {'form': form})

@login_required
def excluir_plano(request, id):
    plano = get_object_or_404(Plano, id=id)
    if request.method == 'POST':
        plano.delete()
        return redirect('listar_planos')
    return render(request, 'planos/excluir.html', {'plano': plano})

# PAGAMENTOS 
@login_required
def listar_pagamentos(request):
    pagamentos = Pagamento.objects.all()
    return render(request, 'pagamentos/listar.html', {'pagamentos': pagamentos})

@login_required
def criar_pagamento(request):
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_pagamentos')
    else:
        form = PagamentoForm()
    return render(request, 'pagamentos/form.html', {'form': form})

@login_required
def editar_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            return redirect('listar_pagamentos')
    else:
        form = PagamentoForm(instance=pagamento)
    return render(request, 'pagamentos/form.html', {'form': form})

@login_required
def excluir_pagamento(request, id):
    pagamento = get_object_or_404(Pagamento, id=id)
    if request.method == 'POST':
        pagamento.delete()
        return redirect('listar_pagamentos')
    return render(request, 'pagamentos/excluir.html', {'pagamento': pagamento})

# TREINOS 
@login_required
def listar_treinos(request):
    treinos = Treino.objects.all()
    return render(request, 'treinos/listar.html', {'treinos': treinos})

@login_required
def criar_treino(request):
    if request.method == 'POST':
        form = TreinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_treinos')
    else:
        form = TreinoForm()
    return render(request, 'treinos/form.html', {'form': form})

@login_required
def editar_treino(request, id):
    treino = get_object_or_404(Treino, id=id)
    if request.method == 'POST':
        form = TreinoForm(request.POST, instance=treino)
        if form.is_valid():
            form.save()
            return redirect('listar_treinos')
    else:
        form = TreinoForm(instance=treino)
    return render(request, 'treinos/form.html', {'form': form})

@login_required
def excluir_treino(request, id):
    treino = get_object_or_404(Treino, id=id)
    if request.method == 'POST':
        treino.delete()
        return redirect('listar_treinos')
    return render(request, 'treinos/excluir.html', {'treino': treino})