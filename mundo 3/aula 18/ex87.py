mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = maior = coluna = 0
for x in range(0, 3):
    for y in range(0, 3):
        mat[x][y] = int(input(f'Digite valores para [{x}, {y}]: '))
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{mat[x][y]:^5}]', end=' ')
        if mat[x][y] % 2 == 0:
            pares += mat[x][y]
    print()
print(f"A soma dos pares é: {pares}")
for x in range(0, 3):
    coluna += mat[x][2]
print(f"Soma dos valores da 3° coluna: {coluna}")
for y in range(0, 3):
    if y == 0:
        maior = mat[1][y]
    elif mat[1][y] > maior:
        maior = mat[1][y]
print(f'O maior valor da segunda linha é: {maior}')
