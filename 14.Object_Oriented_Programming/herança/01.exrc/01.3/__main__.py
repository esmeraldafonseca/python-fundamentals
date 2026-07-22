from rich import print
from aluno import Aluno
from funcionario import Funcionario
from professor import Professor


def main():
    aluno1 = Aluno("Artur", 19, "Filosofia", "MF26")
    aluno1.aniversario()
    aluno1.fazer_matricula()

    professor1 = Professor("Miguel", 57, "Ciencias humanas", "Mestre")
    professor1.aniversario()
    professor1.dar_aula()

    funcionaria1 = Funcionario("Paula", 28, "secretaria", "secretaria")
    funcionaria1.picar_ponto()

if __name__ == "__main__":
    main()
