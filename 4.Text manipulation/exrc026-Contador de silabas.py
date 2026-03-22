frase = str ( input('Digite uma frase')) .upper() .strip()

print('A tua frase tem {}"a"' .format(frase.count('A')))
print('O primeiro "A" está no posição {}' .format(frase.find('A') +1))
print('O ultimo A apareceu na posição {}' .format(frase.rfind('A') +1 ))
