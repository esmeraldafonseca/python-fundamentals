print('-=' * 15)
print('Analisador de triangulos')
print('-=' * 15)

n1 = float(input('Digite o primeiro segmentos'))
n2 = float(input('Digite o segundo segmento'))
n3 = float(input('Digite o terceiro segmento'))

if n1 < n2 + n3 and n2 < n1 + n3 and n3 < n1 + n2:
    print('Os segmentos a cima podem formar um triangula')
else:
    print('Os segmentos a cima NÃO1 formam um tringulo')
