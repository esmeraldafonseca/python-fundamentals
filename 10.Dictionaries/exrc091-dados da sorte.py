from random import randint
from time import sleep
from operator import itemgetter
jogos = {'Jogador 1': randint(1,6),
         'Jogador 2': randint(1,6),
         'Jogador 3': randint(1,6),
         'Jogador 4': randint(1,6) }

ranking = ()
ranking = sorted(jogos.items(), key=itemgetter(1), reverse= True)
"""podemos usar diretamente o sorted para organizar mas o melhor mesmo é organizamos por
em um outro dict"""

print(f'Os valores sorteados foram:')
print("-"*20)
for k,v in jogos.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)

"""Para organizar dict pelos valores e não pelas keys(o que o sorted faz)
 temos que usar da biblioteca operator o metodo itemgetter
 O itemgetter(1) pega os dados pelo valor, mas o 0 pega pelas chaves
 """
print("-="*30)
for i, v in enumerate (ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}. ')

print("=-"*30 )



