import random
maquina = random.randint(0, 10)
print("Vou pensar em um número entre 0 e 10, tenta adinvinhar!")
player = int(input("Em que número eu pensei? "))
print("Analisando...")
if player == maquina:
    print("Parabéns, você acertou!")
else:
    print(f"O número que eu pensei foi {maquina}.")
    print("Você errou, mais sorte na próxima!")