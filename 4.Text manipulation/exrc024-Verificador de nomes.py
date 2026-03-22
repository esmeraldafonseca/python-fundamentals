from os.path import split

city = str(input('Digite o nome da sua cidade')) .strip()

print(city[:6].upper() == 'SANTOS')

'''n = split(city)
SANTO
print(n[0].find('santos'))
'''