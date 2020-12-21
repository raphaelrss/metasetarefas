# Generated by Django 3.1.3 on 2020-12-16 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=8)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('descricao', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Setores',
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('funcao', models.CharField(max_length=25)),
                ('dt_admissao', models.DateField()),
                ('aniversario', models.DateField()),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_entrega', models.DateTimeField()),
                ('descricao', models.TextField()),
                ('terminada', models.BooleanField(default=False)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.estado')),
                ('responsavel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.usuario')),
                ('setor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.setor')),
            ],
        ),
        migrations.CreateModel(
            name='Contato',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('descricao', models.TextField()),
                ('assunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='metas.tarefa')),
                ('para_quem_enviar', models.ManyToManyField(to='metas.Usuario')),
            ],
        ),
    ]
