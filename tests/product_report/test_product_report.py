from inventory_report.inventory.product import Product


def test_relatorio_produto():
    cdb = (Product(
      1,
      "CDB",
      "Banco do Brasil",
      "24/11/2022",
      "23/05/2024",
      "CDB00001C",
      "De preferência em um serviço de nuvem"
    ))

    informacao = (
      "O produto CDB"
      " fabricado em 24/11/2022"
      " por Banco do Brasil"
      " com validade até 23/05/2024"
      " precisa ser armazenado"
      " De preferência em um serviço de nuvem."
    )

    assert cdb.__repr__() == informacao
