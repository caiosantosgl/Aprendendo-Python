cont = ' '
lista = []
while cont not in 'Nn':
    n = int(input("Digite um valor para adicionar na lista: "))
    if n not in lista:
        lista.append(n)
        print("Valor adicionado.")
    else:
        print("Este valor ja foi digitado, portanto, não será adicionado a lista.")
    cont = str(input("Deseja continuar [S/N]? "))
lista.sort()
print(f"Os valores digitados foram: {lista}")
