info = {}
dados = []
som = med = 0
while True:
    info.clear()
    info['nome'] = str(input("Nome: "))
    while True:
        info['sexo'] = str(input("Sexo [M/F]: ")).upper()[0]
        if info['sexo'] not in 'MF':
            print("ERRO! Digite apenas M ou F.")
        if info['sexo'] in 'Mm' or info['sexo'] in 'Ff':
            break
    info['idade'] = int(input("Idade: "))
    som += info['idade']
    dados.append(info.copy())
    while True:
        esc = str(input("Deseja continuar [S/N]? ")).upper()[0]
        if esc in 'SN':
            break
        print("ERRO! Digite apenas S ou N.")
    if esc == 'N':
        break
print("-" * 50)
print(f"{len(dados)} foram cadastrados.")
med = som / len(dados)
print(f"A média de idade é {med:5.2f} anos.")
print("As mulheres cadastradas foram: ", end='')
for p in dados:
    if p['sexo'] in 'Ff':
        print(f'{p['nome']} ', end='')
print()
print("Lista pessoas que estão acima da média: ")
for a in dados:
    if p['idade'] >= med:
        print("    ", end='')
        for c, v in p.items():
            print(f"{c} = {v}; ", end='')
        print()
print('-' * 50)
