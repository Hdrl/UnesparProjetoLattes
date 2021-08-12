from csv import ProjectExtract, xmlHandler

from django.core.management.base import BaseCommand
from lattes.models import *

class Command(BaseCommand):
    args = ""
    help = "comando que popula a tabela Projeto do banco de dados"

    def _create_projects(self):
        print("exluindo projetos...")  
        Projeto.objects.all().delete()
        print("salvando projetos...")
        for p in xmlHandler.all_projects():
            p1 = Projeto(nome = p["NOME"], idCurriculo = p["IDCURRICULO"], anoInicio = p["ANOINICIO"], situacao = p["SITUACAO"], tipo = p["TIPO"], coordenador = p["COORDENADOR"], informadoPor = p["INFORMADOPOR"])
            p1.save()

    def _create_productions(self):
        print("exluindo tabelas...")  
        Producao.objects.all().delete()
        print("salvando producoes...")
        for p in xmlHandler.all_productions():
            p1 = p.production
            p1.save()
            for setor in p.setores:
                setor.save()
            for area in p.areasConchecimento:
                area.save()
            for palavra in p.palavrasChaves:
                palavra.save()

    def handle(self, *args, **options):
        self._create_projects()
        self._create_productions()