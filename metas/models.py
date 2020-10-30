from django.db import models


class Setor(models.Model):
    nome = models.CharField(max_length=25)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name_plural = 'Setores'

class Usuario(models.Model):
    nome = models.CharField(max_length=25)
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    funcao = models.CharField(max_length=25)
    dt_admissao = models.DateField
    aniversario = models.DateField

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    nome = models.CharField(max_length=25)
    data_criacao = models.DateField(auto_now_add=True)
    data_entrega = models.DateField()
    descricao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
