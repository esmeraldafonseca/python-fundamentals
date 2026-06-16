from rich import print

class Pessoas:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1


class Aluno(Pessoas):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"Matricula feita com sucesso, parabens {self.nome}")


class Professor(Pessoas):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel

    def dar_aula(self):
        print(f"A aula acabou de coemçar")


class Funcionario(Pessoas):
    def __init__(self, nome, idade, cargo, setor ):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor
    
    def picar_ponto(self):
        print(f"{self.nome} bateu ponto")


aluno1 = Aluno("Artur", 19, "Filosofia", "MF26")
aluno1.aniversario()
aluno1.fazer_matricula()

professor1 = Professor("Miguel", 57, "Ciencias humanas", "Mestre")
professor1.aniversario()
professor1.dar_aula()

funcionaria1 = Funcionario("Paula", 28, "secretaria", "secretaria")
funcionaria1.picar_ponto()