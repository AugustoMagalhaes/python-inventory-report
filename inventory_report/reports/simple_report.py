from datetime import date


class SimpleReport:
    def __init__(self):
        ...

    @staticmethod
    def filtra_condicao(lista, hoje, condicao):
        if condicao == ">":
            filtro = filter(lambda data: True if data > hoje else False, lista)
        else:
            filtro = filter(lambda data: True if data < hoje else False, lista)
        return min(list(filtro))

    @staticmethod
    def produtos_por_empresa(lista):
        estoque_empresa = {}
        for dado in lista:
            nome_empresa = dado["nome_da_empresa"]
            if nome_empresa in estoque_empresa.keys():
                estoque_empresa[nome_empresa] += 1
            else:
                estoque_empresa[nome_empresa] = 1
        return estoque_empresa

    def empresa_com_mais_produtos(lista):
        produts = SimpleReport.produtos_por_empresa(lista)
        return max(produts, key=produts.get)

    @staticmethod
    def generate(lista):
        hoje = date.today().strftime("%Y-%m-%d")
        datas_fab = list(map(lambda obj: obj["data_de_fabricacao"], lista))
        datas_val = list(map(lambda obj: obj["data_de_validade"], lista))
        fab_mais_antiga = SimpleReport.filtra_condicao(datas_fab, hoje, "<")
        validade_recente = SimpleReport.filtra_condicao(datas_val, hoje, ">")
        empresa_mais_produtos = SimpleReport.empresa_com_mais_produtos(lista)

        return (f'Data de fabricação mais antiga: {fab_mais_antiga}\n'
                f'Data de validade mais próxima: {validade_recente}\n'
                f'Empresa com mais produtos: {empresa_mais_produtos}')
