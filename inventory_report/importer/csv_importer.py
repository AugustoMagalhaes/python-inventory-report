
from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        extensao = path.split(".")[1]
        if extensao == "csv":
            return Inventory.le_arquivo(path)
        else:
            raise ValueError("Arquivo inválido")
