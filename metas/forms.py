from django.forms import ModelForm
from .models import *


class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'data_entrega', 'responsavel', 'setor', 'descricao']

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'descricao']
