from django.db import models

# Create your models here.
class Producao(models.Model):
    ano = models.IntegerField()
    informadoPor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tipoAgrupador = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    tipoVinculo = models.CharField(max_length=255)
    formacao = models.CharField(max_length=255)
    instituicaoEmQueSeFormou = models.CharField(max_length=255)
    anoQueIngressouNoCampus = models.IntegerField()
    descricao = models.CharField(max_length=255)
