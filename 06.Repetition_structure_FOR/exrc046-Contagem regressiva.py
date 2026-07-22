from time import sleep

print('{:=^23}'.format('ANO NOVO'))

n = str(input('''Digite:
[Sim] Para iniciar a contagem
[Não] Para não fazer nada
:''')) .upper()
if n == 'SIM':
    for c in range(10, -1, -1):
        print(c)
        sleep(1)
    print('BUM BUM BUM')
elif n == 'NÃO' :
    print('ok')

else:
    print('Comando invalido')



