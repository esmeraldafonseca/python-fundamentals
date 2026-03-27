from  random import randint
from time import sleep

def sortear(lista):
    print(f'Sorteando 5 valores da lista:', end='')
    for i in range (0,5):

        n = randint(1,10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.3)
    print('PRONTO')




def soma(lista):
    somap =0
    for valor in lista:
        if valor % 2 == 0:
            somap += valor
    print(f'A soma dos valores pares de {lista} é {somap}')

#programa principal
Numeros =[]
sortear(Numeros)
soma(Numeros)
