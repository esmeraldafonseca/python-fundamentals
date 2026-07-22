import math

a = float(input('digite o valor do angulo'))
s = math.sin(math.radians(a))
c = math.cos(math.radians(a))
t = math.tan(math.radians(a))


print('o seu seno é {:.2f}\no coseno é {:.2f}\ne a tangente é {:.2f}'.format(s, c,t))
