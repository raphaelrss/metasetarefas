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
    dt_admissao = models.DateField()
    aniversario = models.DateField()

    def __str__(self):
        return self.nome

class Estado(models.Model):
    nome = models.CharField(max_length=8)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nome

class Passo(models.Model):
    titulo = models.CharField(max_length=40)
    porcentagem = models.DecimalField(decimal_places=2, max_digits=4)
    descricao = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.titulo

class Tarefa(models.Model):
    nome = models.CharField(max_length=30)
    data_criacao = models.DateField(auto_now_add=True)
    data_entrega = models.DateTimeField()
    descricao = models.TextField()
    setor = models.ForeignKey(Setor, on_delete=models.CASCADE)
    responsavel = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    passos = models.ManyToManyField(Passo)

    def __str__(self):
        return self.nome


