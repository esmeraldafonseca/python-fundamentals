import rich
from rich import print

class Funcionario:
    
    empresa = "curso em video"
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    def apresentacao(self):
        return f"Meu nome é [blue]{self.nome}[/] sou {self.cargo} e trabalho no setor {self.setor}da empresa {Funcionario.empresa}"

    # def __str__(self):
    #     return f"Meu nome é {self.nome} sou {self.cargo} e trabalho no setor {self.setor} "
    

# Funcionario.empresa = "hostnet" essa linha muda os valores tbm na classe funcionario

funcionario1 = Funcionario("Maria Tomás", "Academico", "Professora")

funcionario1.empresa = "Mango" #cria um atributo local empresa e da-lhe o valor mango
print(funcionario1.empresa)
print(funcionario1.apresentacao())