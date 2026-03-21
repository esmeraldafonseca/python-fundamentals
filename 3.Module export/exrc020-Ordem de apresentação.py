from random import shuffle

n1 = input('primeiro npome')
n2 = input('segundo nome')
n3 = input('terceiro nome')
n4 = input('quartp nome')

lista = [n1, n2, n3, n4]
shuffle(lista)

print('a ordem de apresentaçã será :')
print(lista)
