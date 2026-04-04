sexo = str(input('Digite o seu genero [M/F]')).upper() .strip()

while sexo != 'F' and sexo != 'M':
    print('Opção invalida')
    sexo = str(input('As opções aceites são [F/M]')).upper()[0] .strip()
print('O seu genero é {}'.format(sexo))

# not in
'''while sexo not in 'MF':
    print('Opção invalida')
    sexo = str(input('As opções aceites são [F/M]')).upper()[0].strip()
print('Sexo {} registrado com sucesso'.format(sexo))
'''