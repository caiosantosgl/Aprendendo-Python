import random
import time
import operator
rank = []
jogador = {'Jogador 1': random.randint(1, 6), 'Jogador 2': random.randint(1, 6), 'Jogador 3': random.randint(1, 6), 'Jogador 4': random.randint(1, 6)}
for c, p in jogador.items():
    print(f"{c} tirou {p} no dado.")
    time.sleep(1)
rank = sorted(jogador.items(), key=operator.itemgetter(1),  reverse=True)
for a, b in enumerate(rank):
    print(f"Em {a + 1} lugar: {b[0]} com {b[1]}.")
    time.sleep(1)
