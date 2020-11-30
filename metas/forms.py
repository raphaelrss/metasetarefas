from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'data_entrega', 'responsavel', 'setor', 'estado', 'descricao', 'terminada']
        widgets = {
            'data_entrega': DateInput(),
        }
