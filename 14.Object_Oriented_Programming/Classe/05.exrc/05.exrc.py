from rich import print
from rich.panel import Panel

class Gamer:

    """
    Uma classe que cria um gamer com nome, nick name e lista os seus jogos favoritos
    """

    def __init__(self,nome, nick_name):
        self.nome = nome 
        self.nick = nick_name 
        self.jogos_favoritos = []

    def __str__(self):
        return f"Nome: {self.nome}\nNick name: {self.nick}\nJogos favoritos: {self.jogos_favoritos}"

    def add_favorito(self, jogo):
        self.jogos_favoritos.append(jogo)
        self.jogos_favoritos = sorted(self.jogos_favoritos, key=str.lower)
        # for i in self.jogos_favoritos:
        #     print(i)

    def ficha(self):
        conteudo = f"Nome: {self.nome}\n"
        conteudo += f"Nick name: {self.nick}\n"
        for jogos in self.jogos_favoritos:
            conteudo += f"Jogos Favoritos: {jogos}\n"
            
        panel = Panel(conteudo, title=self.nick, width= 35)
        print(panel)

gamer1 = Gamer("Ana", "Dumb")
gamer1.add_favorito("bla")
gamer1.add_favorito("bla bla")
gamer1.add_favorito("bla bla bla")
gamer1.ficha()