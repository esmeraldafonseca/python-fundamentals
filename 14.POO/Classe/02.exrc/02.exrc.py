from rich import print
from rich.panel import Panel

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        # nome_formatado = self.nome
        # nome_ainda_mais_formatado = f"{nome_formatado.center(30, "")}"
        preco_formatado = f"£{self.preco:,.2f}"
        panel = Panel(f"{self.nome:^30}\n{"-"*30}\n{preco_formatado:.^30}", title="Produto", width=34)
        print(panel)

telefone = Produto("Iphone 18 pro utra max", 2_130)
telefone.etiqueta()

computador = Produto("Notebook gamer", 6_080)
computador.etiqueta()