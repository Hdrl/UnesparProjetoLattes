from django.db import models

# Create your models here.
class Producao(models.Model):
    ano = models.IntegerField()
    informadoPor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tipoAgrupador = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)