from django.shortcuts import render, redirect
from .models import *
from .forms import TarefaForm, SetorForm, PassoForm
from django.http import HttpResponse


def home(request):
    return render(request, 'metas/home.html')


def listagem(request):
    data = {
        'tarefas': Tarefa.objects.all(),
    }
    return render(request, 'metas/listagem.html', data)


def nova_tarefa(request):
    form = TarefaForm(request.POST or None)
    data = {
        'form': form
    }

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

    return render(request, 'metas/nova_tarefa.html', data)


def update(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    form = TarefaForm(request.POST or None, instance=tarefa)
    data = {
        'tarefa': tarefa,
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'metas/update_tarefa.html', data)


def delete(request, pk):
    tarefa = Tarefa.objects.get(pk=pk)
    tarefa.delete()
    return redirect('url_listagem')

def novo_setor(request):
    form = SetorForm(request.POST or None)
    data = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'metas/novo_setor.html', data)

def vermelho(request):
    tarefas = Tarefa.objects.filter(estado=1)
    data = {
        'tarefas': tarefas,
    }
    return render(request, 'metas/vermelho.html', data)

def novo_passo(request):
    form = PassoForm(request.POST or None)
    data = {
        'form': form
    }
    if form.is_valid():
        form.save()
        return redirect('url_listagem')
    return render(request, 'metas/novo_setor.html', data)
