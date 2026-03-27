from random import randint
from  time import sleep

def maior(*numeros):
    cont = m = 0

    print('-='*30)
    print(f'Analisando os valores passados...')
    for  v in numeros:
        print(f'{v} ', end='')
        sleep(0.5)
        if cont ==0:
            m > v
        else:
            if v > m:
                m=v
        cont +=1
    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {m}')


#progarama principal

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
