esc = ' '
maior18 = conthomem = mulher20 = 0
while True:
    idade = int(input("Digite sua idade: "))
    sexo = str(input("Digite seu sexo [M/F]: ")).strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input("Opção inválida, digite novamente: ")).strip()[0]
    esc = str(input("Deseja continuar [S/N]? ")).strip()[0]
    while esc not in 'SsNn':
        esc = str(input("Opção inválida, digite novamente: ")).strip()[0]
    if sexo in 'Mm':
        conthomem += 1
    if idade >= 18:
        maior18 += 1
    if sexo in 'Ff':
        if idade <= 20:
            mulher20 += 1
    if esc in 'Nn':
        break
print(f"A quantidade de homens é {conthomem}, a quantidade de pessoas com mais de 18 anos é {maior18}, e a quantidade de mulheres com menos de 20 anos é {mulher20}.")
