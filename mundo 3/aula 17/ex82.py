lista = []
par = []
impar = []
while True:
    n = int(input("Digite um número: "))
    opç = str(input("Deseja continuar [S/N]? "))
    lista.append(n)
    if n % 2 == 0:
        par.append(n)
    else:
        impar.append(n)
    if opç in 'Nn':
        break
print(f"A lista completa ficou: {lista}")
print(f"A lista com apenas números pares ficou: {par}")
print(f"A lista com apenas númeors ímpares ficou: {impar}")
