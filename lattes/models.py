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

class Projeto(models.Model):
    nome = models.CharField(max_length=50)
    idCurriculo = models.CharField(max_length=50)
    anoInicio = models.CharField(max_length=4)
    situacao = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    coordenador = models.CharField(max_length=50)
    informadoPor = models.CharField(max_length=50)

    def __str__(self):
        return f"(NOME: {self.nome}, INFORMADOPOR: {self.informadoPor}, TIPO: {self.tipo}, ANOINICIO: {self.anoInicio}, IDCURRICULO: {self.idCurriculo}, SITUAÇÃO:{self.situacao}, COORENADOR:{self.coordenador})"
