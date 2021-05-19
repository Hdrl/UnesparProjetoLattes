from .AbstractXml import AbstractXml, Element
import xml.sax
import re, os

class ProductionHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.file = AbstractXml()
        self.extract = False

    def startDocument(self):
        docName = self._locator.getSystemId()
        self.file.name = re.split('[./]', docName)[-2]

    def startElement(self, name, attrs):
        if self.extract:
           self.file.getProduction(-1).childs.append(Element(name, attrs))

        if name in self.file.typeList.keys():
            self.extract = True
            self.file.addProduction(Element(name, attrs))
        if name == "DADOS-GERAIS":
            self.file.addElement(Element(name,attrs))

    def endElement(self, name):
        if name in self.file.typeList.keys( ):
            self.extract = False   

    def endDocument(self):
        pass

class ProjectHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.projects = []
        self.project = {}
        self.data = Data()
        self.extract = False
        self.reportedBy = ''
        self.IDCurriculo = None

    def startDocument(self):
        docName = self._locator.getSystemId()
        self.IDCurriculo = re.split('[./]', docName)[-2]

    def startElement(self, name, attrs):
        if name == "PROJETO-DE-PESQUISA":
            self.extract = True
            self.project["NOME"] = attrs.getValue(self.data.name)
            self.project["ANOINICIO"] = attrs.getValue(self.data.year)
            self.project["SITUACAO"] = attrs.getValue(self.data.situation)
            self.project["TIPO"] = attrs.getValue(self.data.nature)

        if name == "DADOS-GERAIS":
            self.reportedBy = attrs.getValue(self.data.reportedBy)

        if self.extract:
            if name.find("INTEGRANTES-DO-PROJETO") != -1 and attrs.getValue("FLAG-RESPONSAVEL")=="SIM":
                self.project["COORDENADOR"] = attrs.getValue("NOME-COMPLETO")

    def endElement(self, name):
        if name in "PROJETO-DE-PESQUISA":
            self.extract = False
            self.project["INFORMADOPOR"] = self.reportedBy
            self.project["IDCURRICULO"] = self.IDCurriculo
            self.projects.append(self.project)
            self.project = {}
    
    def endDocument(self):
        pass

class Data():
    def __init__(self):
        self.name = "NOME-DO-PROJETO"
        self.year = "ANO-INICIO"
        self.situation  = "SITUACAO"
        self.nature = "NATUREZA"
        self.reportedBy = "NOME-COMPLETO"
        self.ID = "NUMERO-IDENTIFICADOR"

xml_dir = "csv/xmlstest"

def all_projects():
    print("starting get_all_projects...")
    tmp = []
    for file in os.listdir(xml_dir):
        tmp = tmp + get_project(f"{xml_dir}/{file}")
    print("done...")
    return tmp

def all_productions():
    print("starting get_all_productions...")
    tmp = []
    for file in os.listdir(xml_dir):
        list = get_production(f"{xml_dir}/{file}")
        if  list:
            tmp = tmp + list
    print("done...")
    return tmp

def get_project(filePath):
    handler = ProjectHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(filePath)
    return handler.projects

def get_production(filePath):
    handler = ProductionHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(filePath)
    return handler.file.getProductions()