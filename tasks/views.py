from django.shortcuts import render, get_object_or_404
from .models import Tarefa

# Create your views here.

def listar_tarefas(request):
    tarefas = Tarefa.objects.all().order_by('-criado_em')
    return render(request, 'tasks/listar.html', {'tarefas': tarefas})

def detalhes_tarefa(request, pk):
    tarefa = get_object_or_404(Tarefa, pk=pk)
    return render(request, 'tasks/detalhes.html', {'tarefa': tarefa})
