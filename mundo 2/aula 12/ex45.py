import random
opcoes = ['Pedra', 'Papel', 'Tesoura']
maquina = random.randint(0, 2)
print('''Escolha uma opção:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
player = int(input("Escolha sua jogada: "))
print(f"O computador escolheu: {opcoes[maquina]}.")
print(f"Você escolheu {opcoes[player]}.")
if maquina == 0:
    if player == 0:
        print("Empate.")
    elif player == 1:
        print("Você ganhou!")
    elif player == 2:
        print("Você perdeu!")
    else:
        print("Escolha inválida!")
elif maquina == 1:
    if player == 0:
        print("Você perdeu!")
    elif player == 1:
        print("Empate.")
    elif player == 2:
        print("Você ganhou!")
    else:
        print("Escolha inválida!")
elif maquina == 2:
    if player == 0:
        print("Você ganhou!")
    elif player == 1:
        print("Você perdeu!")
    elif player == 2:
        print("Empate.")
    else:
        print("Escolha inválida!")
else:
    print("Escolha inválida!")