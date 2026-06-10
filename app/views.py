from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from .models import Aluno
from .forms import AlunoForm
from django.contrib.auth.decorators import login_required


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