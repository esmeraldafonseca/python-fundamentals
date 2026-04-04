prod = float(input(' qual é o preço do produto?'))
aum = float(prod + (prod * 0.15))
desc = float(prod * 0.08)

print('se pagares a vista recebes um desconto de 8% e ele ficará a {:.2f}' .format( prod - desc))
print(' se parcelares terá um aumento de 15% e ele ficará por {:.2f}' .format(aum))
