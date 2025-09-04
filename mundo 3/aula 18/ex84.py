pessoas =[]
info = []
qntP = 0
maior = menor = 0
while True:
    info.append(str(input("Digite o nome: ")))
    info.append(float(input("Digite a peso: ")))
    if len(pessoas) == 0:
        maior = menor = info[1]
    else:
        if info[1] > maior:
            maior = menor = info[1]
        if info[1] < menor:
            menor = info[1]
    pessoas.append(info[:])
    info.clear()
    esc = str(input("Deseja continuar [S/N]? "))
    qntP += 1
    if esc in 'Nn':
        break
print(f"O total de pessoas cadastradas foram: {qntP}")
print(f"O maior peso é: {maior}Kg. ", end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{p[0]} ', end='')
print()
print(f"O menor peso é: {menor}Kg. ", end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{p[0]} ', end='')
print()
