num = int(input("Digite um número para calcular o fatorial: "))
cont = num
fat = 1
print(f'{num}! = ', end='')
while cont > 0:
    print(f'{cont}', end=" ")
    print(' x ' if cont > 1 else ' = ', end=' ')
    fat *= cont
    cont -= 1
print(fat)
