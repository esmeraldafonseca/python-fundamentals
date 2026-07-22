player = {}
golos = []
time = []

while True:
    player.clear()
    player ['Nome'] = str(input("Nome do jogador: "))
    jogos = int(input(f'Quantas partidas o {player['Nome']} jogou: '))
    golos.clear()
    for i in range(0, jogos):
        golos.append(int(input(f'  Quantos golos na partida {i}: ')))

    player['Golos'] = golos[:]
    player['Total'] = sum(golos)

    time.append(player.copy())


    resposta = str(input("Quer continuar [S/N]? ")).upper()[0]
    while resposta not in "SN":
        print("Resposta invalida. Tente S or N")
        resposta = str(input("Quer continuar [S/N]? ")).upper()[0]
    if resposta == "N":
        break

print("-="*30)
print('cod ', end='')
for i in player.keys():
    print(f'{i:<15}', end='')
print()
print("-"*35)
for k, v in enumerate(time):
    print(f'{k:<3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print("-"*35)

while True:
    busca = int(input("Mostrar dados de qual jogador?(999 para parar)"))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO! Não existe jogador {busca}')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Golos']):
            print(f'    No jogo{i+1} fez {g} golos')
    print("-"*35)
print('         <<<FIM>>>>')


