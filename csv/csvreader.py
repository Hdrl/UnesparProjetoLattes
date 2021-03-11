import csv
from lattes.models import Producao

with open('C:\\Users\\Pichau\\Documents\\Estudos\\html-css\\Projetos\\UnesparProjetoLattes\\csv\\producao.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for line in csv_reader:
        p = Producao(ano=line[1], informadoPor=line[5], tipo=line[6], tipoAgrupador=line[7], titulo=line[8])
        p.save()