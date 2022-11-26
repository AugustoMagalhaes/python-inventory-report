import csv
import json

import xmltodict

from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class Inventory:
    @staticmethod
    def le_arquivo(path):
        tipo_arquivo = path.split(".")[1]
        with open(path) as arquivo:
            if tipo_arquivo == "json":
                arquivo_json = json.load(arquivo)
                return arquivo_json
            elif tipo_arquivo == "csv":
                arquivo_csv = csv.DictReader(arquivo)
                resultado = list(arquivo_csv)
                return resultado
            elif tipo_arquivo == 'xml':
                arquivo_xml = (xmltodict.parse
                               (arquivo.read())["dataset"]["record"])
                return arquivo_xml
            raise NotImplementedError

    @staticmethod
    def import_data(path, tipo_relatorio):
        arquivo = Inventory.le_arquivo(path)
        if tipo_relatorio == "simples":
            relatorio = SimpleReport.generate(arquivo)
            return relatorio
        elif tipo_relatorio == "completo":
            relatorio = CompleteReport.generate(arquivo)
            return relatorio
        else:
            raise Exception("Tipo de relatório inválido")
