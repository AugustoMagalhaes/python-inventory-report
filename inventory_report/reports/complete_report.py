
from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):

    @staticmethod
    def concatena_entries(entries):
        empresa_produtos = ""
        for entry in entries:
            empresa_produtos += "- " + entry[0] + ": " + str(entry[1]) + "\n"
        print("resultado: ", empresa_produtos)
        return empresa_produtos

    @staticmethod
    def generate(lista):
        relatorio_simples = SimpleReport.generate(lista)
        estoque_empresas = SimpleReport.produtos_por_empresa(lista)
        estoque_entries = list(estoque_empresas.items())
        str_estoque_entries = CompleteReport.concatena_entries(estoque_entries)

        return (f"{relatorio_simples}\n"
                f"Produtos estocados por empresa:\n"
                f"{str_estoque_entries}")
