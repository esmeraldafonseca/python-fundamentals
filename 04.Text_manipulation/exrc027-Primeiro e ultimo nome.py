from os.path import split

nome = str(input('Digite o seu nome completo:')) .strip() .capitalize()

separador = nome.split()

print('Muito prazer {}' .format(nome))
print('O seu primeiro nome é {}' .format(separador[0]))
print('E o seu ultimo nome é {}' .format(separador[len(separador) -1]))

