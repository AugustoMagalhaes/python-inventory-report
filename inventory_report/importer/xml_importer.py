

from inventory_report.importer.importer import Importer
from inventory_report.inventory.inventory import Inventory


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        extensao = path.split(".")[1]
        if extensao == "xml":
            arquivo = Inventory.le_arquivo(path)
            return arquivo
        else:
            raise ValueError("Arquivo inválido")
