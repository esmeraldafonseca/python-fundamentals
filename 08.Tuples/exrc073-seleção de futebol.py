
times = 'Benfica', 'Sporting', 'Porto', 'Barcelona', 'Real Madrid', 'Petro de luanda', '1º de Agosto', 'Tondela'

print(times)
print(sorted(times))
print(f'Os 2 primeiros são: {times[:2]}')
print(f'Os 2 ultimos são: {times[-2:]}')

print(f'O Porto encontra-se na posição {times.index("Porto") + 1} º')