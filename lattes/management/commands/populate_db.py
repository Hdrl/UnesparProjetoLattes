from csv import ProjectExtract, xmlHandler

from django.core.management.base import BaseCommand
from lattes.models import Producao, Projeto


class Command(BaseCommand):
    args = ""
    help = "comando que popula a tabela Projeto do banco de dados"

    def _create_projects(self):
        Projeto.objects.all().delete()
        for p in xmlHandler.all_projects():
            p1 = Projeto(nome = p["NOME"], idCurriculo = p["IDCURRICULO"], anoInicio = p["ANOINICIO"], situacao = p["SITUACAO"], tipo = p["TIPO"], coordenador = p["COORDENADOR"], informadoPor = p["INFORMADOPOR"])
            p1.save()

    def _create_productions(self):
        Producao.objects.all().delete()
        for p in xmlHandler.all_productions():
            p1 = Producao(ano=p["ANO"], informadoPor=p["INFORMADOPOR"], tipo=p["TIPO"], tipoAgrupador=p["TIPOAGRUPADOR"], titulo=p["TITULO"])
            p1.save()

    def handle(self, *args, **options):
        self._create_projects()
        self._create_productions()
