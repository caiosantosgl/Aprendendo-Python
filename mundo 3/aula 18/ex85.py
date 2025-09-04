lista = [[], []]
for z in range(1, 8):
    n = int(input(f"Digite o {z}° valor: "))
    if n % 2 == 0:
        lista[0].append(n)
    else:
        lista[1].append(n)
lista[0].sort()
lista[1].sort()
print(f"Os valores pares foram: {lista[0]}")
print(f"Os valores ímpares foram: {lista[1]}")
