from abc import ABC, abstractmethod

class Pessoas(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self): #metodo concreto
        self.idade += 1
    
    @abstractmethod #metodo abstrato
    def estudar(self):
        pass


class Aluno(Pessoas):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"Matricula feita com sucesso, parabens {self.nome}")

    
    def estudar(self):
        print(f"{self.nome} está a estudar {self.curso} na turma {self.turma}")
   


class Professor(Pessoas):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"A aula acabou de começar")

    def estudar(self):
        print(f"{self.nome} é especialista em {self.especialidade} no {self.nivel}")


class Funcionario(Pessoas):
    def __init__(self, nome, idade, cargo, setor ):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def picar_ponto(self):
        print(f"{self.nome} bateu ponto")


    def estudar(self):
        print(f"{self.nome} se especializa na area de {self.cargo}")
       