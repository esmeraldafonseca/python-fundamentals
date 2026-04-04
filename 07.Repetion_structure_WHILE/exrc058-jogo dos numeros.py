from random import randint
computador = randint(0,10)
tentativas = 0

print('Sou o seu computador... Acabei de pensar em um numero entre 0 e 10!\n')
print('Será que você consegue adivinhar qual foi?')
n = int (input('Qual foi o seu palpite?:'))

while n != computador :
    tentativas += 1
    if n < computador :
        print('Estás perto, tenta subir um pouco mais')
        n = int(input('Qual é o teu palpite agora?: '))
    else:
        print('Estás perto, tenta descer um pouco masi')
        n = int(input('Qual é o teu palpite agora?: '))


print('GANHASTE')
print('Eu pensei em {} e tu digitaste {}. PARABENS'.format(computador, n))
print('So tiveste que tentar {} vezes LOL'.format(tentativas))

