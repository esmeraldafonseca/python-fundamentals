from aluno import *

def main():
    alunos =[
        {"Nome": "Ana", "Notas": 12},
        {"Nome": "Mario", "Notas":9 },
        {"Nome": "Rui", "Notas": 10},
        {"Nome": "Maria", "Notas": 18},
        {"Nome": "Paula", "Notas": 11}
    ]

    guardar_alunos(alunos)
    aluno = carregar_alunos()

    print(f'A media da turma é de :{media_turma(aluno)}')
    nomes = aprovados_alunos(aluno)
    print(f'Aprovados: {nomes}')
    


if __name__=="__main__":
    main()