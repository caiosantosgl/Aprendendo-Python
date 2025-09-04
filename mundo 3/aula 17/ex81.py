lista = []
qntN = 0
while True:
    n = int(input("Digite um número: "))
    opç = str(input("Deseja continuar [S/N]? "))
    if opç in 'Nn':
        break
    lista.append(n)
    qntN += 1
print(f"A quantidade de números digitados foram: {qntN}")
lista.sort(reverse=True)
print(f"A lista dos números em ordem decrescente é: {lista}")
if 5 in lista:
    print("O número 5 faz parte da lista.")
else:
    print("O número 5 não faz parte da lista.")
