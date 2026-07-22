n1 = int(input('Digite um numero: '))

print('Para qual sistema queres converter o numero digitado?')
print('1 para binario\n2 para otal\n3 para hexadecimal')
n2 = int(input('Digite :'))
if n2 == 1 :
    print('{} convertido para binario é {}'.format(n1, bin(n1)[2:]))

elif n2 == 2 :
  print('{} convertido para octal é {}'.format(n1, oct(n1)[2:]))

elif n2 == 3 :
  print('{} covertido para hexadecimal é {}'.format(n1, hex(n1)[2:]))

else:
    print('Tens que escolher um dos numeros acima')