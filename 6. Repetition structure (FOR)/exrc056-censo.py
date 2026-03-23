somadasidade = 0
mediaidade = 0
velhoidade = 0
velhonome = 0
jovemidade = 0
for n in range(1, 5):
    print('='  * 30)
    print('{:^7} {}ª PESSOA'.format('', n))
    print('=' * 30)
    idade = int(input('Digite a sua idade: '))
    nome = str(input('Digite o nome: ')) .strip()
    genero = str(input('Digite o genro [M/F]:')).strip() .upper()
    somadasidade += idade


    if n == 1 and genero == 'M':
        velhoidade += idade
        velhonome += nome
    else:
        if velhoidade < idade and genero == 'M':
            velhoidade = idade
            velhonome = nome

    if genero == 'F' and idade < 20:
        jovemidade += 1

mediaidade = somadasidade/4
print('Há {} mulheres menores de 20 anos'.format(jovemidade))
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homem mais velho é {} e tem {} anos'.format(velhonome, velhoidade))


