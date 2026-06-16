from Avaliacao import *

def main():
    aluno1 = Avaliacao("Pedro", "Matematica")
    aluno1.nota = -3
    print(f'{aluno1.nome} teve {aluno1.nota} em {aluno1.disciplina}')

if __name__ == "__main__":
    main()