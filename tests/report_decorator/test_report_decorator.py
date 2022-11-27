from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport


def test_decorar_relatorio():
    json_mockado = [
        {
            "id": "8",
            "nome_do_produto": "Aspirin",
            "nome_da_empresa": "Galena Biopharma",
            "data_de_fabricacao": "2021-02-22",
            "data_de_validade": "2024-03-14",
            "numero_de_serie": "KZ63 800H NM4B ZOWB YYUI",
            "instrucoes_de_armazenamento": "instrucao 8"
        }
    ]

    relatorio_colorido = ColoredReport(SimpleReport)
    relatorio = relatorio_colorido.generate(json_mockado)
    json_assert = json_mockado[0]

    assert (
      relatorio
      ==
      f"\033[32mData de fabricação mais antiga:\033[0m "
      f"\033[36m{json_assert['data_de_fabricacao']}\033[0m"
      f"\n\033[32mData de validade mais próxima:\033[0m "
      f"\033[36m{json_assert['data_de_validade']}\033[0m"
      f"\n\033[32mEmpresa com mais produtos:\033[0m "
      f"\033[31m{json_assert['nome_da_empresa']}\033[0m"
    )
