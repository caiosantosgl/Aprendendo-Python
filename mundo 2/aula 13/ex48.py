somatoria = 0
cont = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        somatoria = somatoria + n
        cont = cont + 1
print(f"A somatoria de todos os {cont} números solicitados é: {somatoria}.")