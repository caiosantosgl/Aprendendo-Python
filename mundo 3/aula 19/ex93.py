jogador = {}
partidas = []
jogador['nome'] = str(input("Nome do jogador: "))
total = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
cont = 1
while cont <= total:
    partidas.append(int(input(f"Quantos gols na partida {cont}? ")))
    cont += 1
jogador['gols'] = partidas[:]
jogador['total'] = sum(partidas)
print('-' * 30)
print(jogador)
print('-' * 30)
for c, v in jogador.items():
    print(f"O campo {c} tem o valor {v}.")
print('-' * 30)
for c, v in enumerate(jogador['gols']):
    print(f"-> Na partida {c}, fez {v} gols.")
print(f"Foi um total de {jogador['total']} gols.")
print('-' * 30)