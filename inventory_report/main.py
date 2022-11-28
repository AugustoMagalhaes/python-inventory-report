import sys

from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor


def get_importer(importer):
    importer_map = {
        'csv': CsvImporter,
        'json': JsonImporter,
        'xml': XmlImporter,
    }
    try:
        return importer_map[importer]
    except KeyError:
        print(f"importer '{importer}' não encontrado")


def get_args():
    return sys.argv[1:]


def main():
    if len(sys.argv) != 3:
        sys.stderr.write("Verifique os argumentos\n")
    else:
        args_validos = get_args()
        path, tipo_relatorio = args_validos

        extensao = path.split('.')[1]
        inventory_refactor = InventoryRefactor(get_importer(extensao))
        relatorio = inventory_refactor.import_data(path, tipo_relatorio)

        print(relatorio, end="")
