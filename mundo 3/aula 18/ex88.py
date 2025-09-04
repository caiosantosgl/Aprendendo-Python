import random
import time
lista = []
jogos = []
qnt = int(input("Digite a quantidade de jogos: "))
cont2 = 1
while cont2 <= qnt:
    cont1 = 0
    while True:
        vals = random.randint(1, 60)
        if vals not in lista:
            lista.append(vals)
            cont1 += 1
        if cont1 >= 6:
            break
    jogos.append(lista[:])
    lista.clear()
    cont2 += 1
print('-=' * 30)
for a, b in enumerate(jogos):
    print(f'{a+1}° jogo: {b}')
    time.sleep(1)
print('-=' * 30)
