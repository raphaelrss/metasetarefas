from django.shortcuts import render, redirect
from .models import *
from .forms import TarefaForm, ContatoForm


def home(request):
    return render(request, 'metas/home.html')


def listagem(request):
    form = TarefaForm(request.POST or None)
    contatoForm = ContatoForm(request.POST or None)
    data = {
        'tarefas': Tarefa.objects.all(),
        'form': form,
        'formContato': contatoForm,
    }
    if contatoForm.is_valid():
        contatoForm.save()

        return redirect('url_listagem')

    if form.is_valid():
        form.save()
        return redirect('url_listagem')

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

def lista_contatos(request):
    contatos = Contato.objects.all()
    data = {
        'contatos': contatos,
    }
    return render(request, 'metas/contatos.html', data)
