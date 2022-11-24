from inventory_report.inventory.product import Product


def test_cria_produto():
    cdb = (Product(
      1,
      "CDB",
      "Banco do Brasil",
      "24/11/2022",
      "23/05/2024",
      "CDB00001C",
      "De preferências em um serviço de nuvem com três zonas " +
      "de disponibilidade"
    ))

    assert cdb.id == 1
    assert cdb.id != 2
    assert cdb.nome_do_produto == "CDB"
    assert cdb.data_de_fabricacao == "24/11/2022"
    assert cdb.data_de_validade == "23/05/2024"
    assert cdb.numero_de_serie == "CDB00001C"
    assert cdb.instrucoes_de_armazenamento == (
     "De preferências em um serviço de nuvem com três zonas de disponibilidade"
     )
