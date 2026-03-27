from time import sleep

def contador(inicio, fim, passo):
    if passo < 0:
        passo *= -1
    if passo == 0:
        passo =1
    print("-" *32)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        cont = inicio
        while cont <= fim:
            print(f'{cont} ', end='')
            sleep(0.5)
            cont += passo
        print("Fim.")
    else:
        cont = inicio
        while cont >= fim:
            sleep(0.5)
            print(f'{cont} ', end='')
            cont -= passo
        print("Fim.")

    print("=" * 32)

#programa principal
contador(1, 10, 1)

contador(10, 0, 2)

inicio = int(input("INICIO: "))
fim = int(input("FIM: "))
passo= int(input("PASSO: "))
contador(inicio, fim, passo)
