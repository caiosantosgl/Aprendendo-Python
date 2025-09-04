from random import randint
from time import sleep

def sorteia(lst):
    print("Selecionando 5 valores: ", end='')
    for c in range(0, 5):
        a = randint(1, 10)
        lst.append(a)
        print(f'{a} ',  end='', flush=True)
        sleep(0.5)
    print("FIM")
def somaPar(lst):
    som = 0
    for v in lst:
        if v % 2 == 0:
            som += v
    print(f"A soma dos valores pares de {lst} é {som}")

numeros = []
sorteia(numeros)
somaPar(numeros)
