lista = []
for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if i == 0:
        lista.append(num)
        print("Primeiro número adicionado.")
    elif num > lista[len(lista)-1]:
        lista.append(num)
        print("Adicionado ao final da lista.")
    else:
        f = 0
        while f < len(lista):
            if num <= lista[f]:
                lista.insert(f, num)
                print(f"Adiciona na posição {f} da lista.")
                break
            f += 1
print(f"Os valores adicionados na lista em ordem foram: {lista}")
