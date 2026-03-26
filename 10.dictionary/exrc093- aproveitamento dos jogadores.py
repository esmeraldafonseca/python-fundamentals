player = {}
golos = []

player ['Nome'] = str(input("Nome do jogador: "))
jogos = int(input(f'Quantas partidas o {player['Nome']} jogou: '))

for i in range(0, jogos):
    golos.append(int(input(f'  Quantos golos na partida {i}: ')))

player['Golos'] = golos[:]
player['Total'] = sum(golos)
print(player)

print("-="*30)
for k,v in player.items():
    print(f'O campo {k} tem o valor {v}')
print("-="*30)

print(f'O jogador {player['Nome']} jogou {jogos} partidas')
for i, v in enumerate (player['Golos']):
    print(f'    => Na partida {i+ 1} fez {v} golos.')

print(f'Foi um total de {jogos} jogos')