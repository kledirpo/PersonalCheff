from django.db import models
from datetime import datetime

# A Classe abaixo junto com os parametros será a responsavel pela criação das tabelas no banco de dados.

class Receitas (models.Model):
    nome_receita = models.CharField(max_length=100)
    video = models.CharField(max_length=80)
    modo_prepato = models.TextField()
    ingredientes = models.TextField()
    nota = models.IntegerField()
    data_receita = models.DateTimeField(default=datetime.now, blank=True)
# Create your models here.
