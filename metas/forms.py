from django.forms import ModelForm
from django import forms
from .models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class TarefaForm(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'data_entrega', 'responsavel', 'setor', 'estado', 'passos', 'descricao']
        widgets = {
            'data_entrega': DateInput(),
        }

class SetorForm(ModelForm):
    class Meta:
        model = Setor
        fields = ['nome', 'descricao']

class PassoForm(ModelForm):
    class Meta:
        model = Passo
        fields = ['titulo', 'porcentagem', 'descricao']
