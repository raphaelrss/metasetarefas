# Generated by Django 3.1.3 on 2020-11-24 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarefa',
            name='terminada',
            field=models.BooleanField(default=False),
        ),
    ]
