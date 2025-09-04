mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for x in range(0, 3):
    for y in range(0, 3):
        mat[x][y] = int(input(f'Digite valores para [{x}, {y}]: '))
for x in range(0, 3):
    for y in range(0, 3):
        print(f'[{mat[x][y]:^5}]', end=' ')
    print()
