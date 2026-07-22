from pessoas import Pessoas

class Aluno(Pessoas):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)

        self.curso = curso
        self.turma = turma

    def fazer_matricula(self):
        print(f"Matricula feita com sucesso, parabens {self.nome}")
