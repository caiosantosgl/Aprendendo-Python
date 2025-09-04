lista = []
while True:
    n = int(input("Digite um valor para adicionar na lista: "))
    if n not in lista:
        lista.append(n)
        print("Número adicionado.")
    else:
        print("Este valor ja foi digitado, portanto, não será adicionado a lista.")
    opç = str(input("Deseja continuar [S/N]? "))
    if opç in 'Nn':
        break
lista.sort()
print(f"Os valores digitados foram: {lista}")
