n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota:'))
media  = (n1 + n2) / 2


if media < 5.0:
    print('Estás reprovado. A sua media foi {:.1f}.' .format(media))

elif media < 7:
    print('A sua media foi de {:.1f}. Esta de recuperação'.format(media))

else:
    print('A sua media foi de {:.1f}. Etsás aprovado'.format(media))

