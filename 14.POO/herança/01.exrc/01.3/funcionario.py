from pessoas import Pessoas

class Funcionario(Pessoas):
    def __init__(self, nome, idade, cargo, setor ):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def picar_ponto(self):
        print(f"{self.nome} bateu ponto")