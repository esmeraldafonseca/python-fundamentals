from rich import print
from rich.panel import Panel

class Churrasco:
    #Atributos de classe
    CONSUMO_PADRAO = 0.400
    PRECO_CARNE = 5
    def __init__(self, titulo="Churrasco", numero_de_pessoas=1):
        self.titulo = titulo
        self.n_pessoas = numero_de_pessoas

    def __str__(self):
        return f"Esse é {self.titulo} com {self.n_pessoas} pessoas"
    
   
    def quantidade_carne(self):
        return Churrasco.CONSUMO_PADRAO * self.n_pessoas
    
    def preco_total(self):
        return self.quantidade_carne() * self.__class__.PRECO_CARNE

    def total_por_pessoa(self):
        return self.preco_total() / self.n_pessoas
    
    def analisar(self):
        panel = Panel(f"""A analisar [green]{self.titulo}[/], com [blue]{self.n_pessoas}[/] pessoas.
Cada pessoa come aproximadamente em média {Churrasco.CONSUMO_PADRAO}kg e cada kg custa {Churrasco.PRECO_CARNE:,.2f}£
Recomendo [blue]comprar {self.quantidade_carne():,.3f} kg[/] de carne.
O custo total será de [green]{self.preco_total():,.2f}£[/]
Cada pessoa pagará [yellow]{self.total_por_pessoa():,.2f}£[/] para participar"""
                      , title=self.titulo, width=80 )
        print(panel)


a1 = Churrasco("Churras", 15)
a1.analisar()