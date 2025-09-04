import random
maquina = random.randint(1, 10)
print("Pensei em um número entre 1 e 10, tenta adivinhar!")
player = int(input("Digite seu palpite: "))
tentativas = 0
while player != maquina:
    player = int(input("Valor errado, tente outro: "))
    tentativas += 1
print(f"""O número que eu escolhi foi {maquina}.
Parabéns, você acertou!
Você tentou {tentativas} vezes.""")
