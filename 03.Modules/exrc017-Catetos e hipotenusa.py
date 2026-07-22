'''from math import pow, sqrt

o = float(input('Digite o valor do cateto oposto'))
a = float(input('digite o valor do cateto adjacente'))
h = sqrt (pow(o, 2) + pow(a, 2))
print(' a hipotenuza de  {} e {} é {:.2f}'.format(o, a, h))
'''

from math import hypot

o = float(input('digite o valor do cateto oposto'))
a = float(input('digite o valor do cateto adjacente'))
hi = hypot(o, a)
print('o valor da hipotenusa é {}'.format(hi))

