print('=' *31)
print('NUMEROS PRIMOS')
print('=' * 31)

n1 = int(input('Digite um numero:'))
primo = 0
for n in range(1, n1 + 1):
    if n1 % n == 0 :
        primo += 1

if primo == 2:
    print('O numero digitado é primo')
else:
    print('Não é primo')

