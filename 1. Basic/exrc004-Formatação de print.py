texto = input('Digite algo')

print('o tipo primitivo desse valor é', type(texto))

print('{} é uma alfabetico?' .format(texto), texto.isalpha())
print('{} tem todos os carateres maiusculos??' .format(texto), texto.isupper())
print('{} tem tudo minusculo?' .format(texto) ,texto.islower())
print('esta capitalizada?', texto.istitle())
print('só tem espaços?', texto.isspace())
print('{} é um número?' .format(texto), texto.isnumeric())
print('{} é um numero decimal?' .format(texto), texto.isdecimal())
print('{} é alfanumerico?' .format(texto), texto.isalnum())
print('{} é um numero digital??' .format(texto), texto.isdigit())

