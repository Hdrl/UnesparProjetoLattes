from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField

# Create your models here.

class Producao(models.Model):
    ano = models.IntegerField()
    informadoPor = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    tipoAgrupador = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"TITULO = {self.titulo}, ANO = {self.ano}, INFORMADOPOR = {self.informadoPor}"

class Pessoas(models.Model):
    nome = models.CharField(max_length=255)
    titulo = models.CharField(max_length=255)
    campus = models.CharField(max_length=255)
    ano_conclusao = models.CharField(max_length=255)
    vinculo_data = models.CharField(max_length=255)
    vinculo_data_inicio = models.CharField(max_length=255)
    tipo_vinculo = models.CharField(max_length=255)
    outro_vinculo = models.CharField(max_length=255)
    enquadramento = models.CharField(max_length=255)
    outro_enquadramento = models.CharField(max_length=255)
    faculdade_formacao = models.CharField(max_length=255)
    curso_formacao = models.CharField(max_length=255)
    #srcImage = models.ImageField(upload_to='pessoas')
    resumo = models.TextField()
    last_update = models.CharField(max_length=255)
     
    tipoVinculo = models.CharField(max_length=255)
    formacao = models.CharField(max_length=255)
    instituicaoEmQueSeFormou = models.CharField(max_length=255)
    anoQueIngressouNoCampus = models.CharField(max_length=255)
    descricao = models.TextField()
class SetorAtividade(models.Model):
    setor = models.CharField(max_length=45)
    producao_id = models.ForeignKey(Producao, on_delete=models.CASCADE, related_name="setores_atividade")

class PalavraChave(models.Model):
    palavra = models.CharField(max_length=45)
    producao_id = models.ForeignKey(Producao, on_delete=models.CASCADE, related_name="palavrasChave")

class AreaConhecimento(models.Model):
    grandeArea = models.CharField(max_length=45)
    area = models.CharField(max_length=45)
    subArea = models.CharField(max_length=45)
    especialidade = models.CharField(max_length=45)
    producao_id = models.ForeignKey(Producao, on_delete=models.CASCADE, related_name="areas_conhecimento")

class Autor(models.Model):
    nomeCompleto = models.CharField(max_length=45)
    nomeCitacao = models.CharField(max_length=45)
    idCNPQ = models.CharField(max_length=45)

class ProducaoAutor(models.Model):
    producao_id = models.ForeignKey(Producao, on_delete=models.CASCADE, related_name = "producoes")
    autor_id = models.ForeignKey(Autor, on_delete=models.CASCADE, related_name= "Autores")
    ordemAutoria = models.CharField(max_length=45)

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

