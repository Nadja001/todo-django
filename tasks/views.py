from django.shortcuts import render, get_object_or_404, redirect
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-criado_em')
    return render(request, 'tasks/listar.html', {'tarefas': tarefas})

def detalhes_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tasks/detalhes.html', {'tarefa': tarefa})

def criar_tarefa(request):
    tarefa = None
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        tarefa = Tarefa(titulo=titulo, descricao=descricao)
        tarefa.save()
        return redirect('tasks:listar')

    return render(request, 'tasks/criar.html', {'tarefa': tarefa})

def editar_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    if request.method == 'POST':
        titulo = request.POST['titulo']
        descricao = request.POST['descricao']
        concluida = request.POST['concluida']
        tarefa.titulo = titulo
        tarefa.descricao = descricao
        tarefa.concluida = concluida
        tarefa.save()
        return redirect('tasks:listar')

    return render(request, 'tasks/criar.html', {'tarefa': tarefa})

def excluir_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    tarefa.delete()
    return redirect('tasks:listar')
