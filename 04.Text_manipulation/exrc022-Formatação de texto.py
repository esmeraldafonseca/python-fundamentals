from os.path import split

nome = str(input('Digite o seu nome')).strip()

print('Seu nome em minusculas é {}'.format(nome.lower()))
print('Seu nome em maiuscula é {}' .format(nome.upper()))
print('O seu nome é {} e tem {} letras'.format(nome, len(nome) - nome.count(' ')))
print(len(nome))

# o primeir ' ' vai parar no final do primeiro nome e como eliminamos os espaços antes e depois é tbm o tamanho o primeiro noem
print('O seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = split(nome)
print('O seu primeiro nome é {} e tem {} letras'.format(separa[0], len(separa[0])))
