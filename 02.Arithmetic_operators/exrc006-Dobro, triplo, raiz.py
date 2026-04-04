n1 = int(input('Digite um número'))

d = n1*2
t = n1*3
r = n1 ** (1/2)

#print('O dobro é {} \nO triplo é {} \nA raiz quadrada é {}' .format(d, t, r))
print('O dobro é {} \nO triplo é {} \nA raiz quadrada é {}' .format(d, t, pow(n1,(1/2))))
