from collections.abc import Iterable

from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def __iter__(self):
        return InventoryIterator(self.data)

    def import_data(self, path, tipo_relatorio):
        self.data.extend(self.importer.import_data(path))
        class_map = {"simples": SimpleReport, "completo": CompleteReport}

        return class_map[tipo_relatorio].generate(self.data)
