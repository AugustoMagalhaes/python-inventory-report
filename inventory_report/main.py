import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter


def get_importer(importer):
    importer_map = {
        'csv': CsvImporter,
        'json': JsonImporter,
        'xml': XmlImporter,
    }
    try:
        return importer_map[importer]
    except KeyError:
        print(f"{importer} não encontrado")


def get_args():
    return sys.argv[:1]


def main():
    lista_args = get_args()

