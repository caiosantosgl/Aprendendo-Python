esc = ' '
totalcompra = produtos1000 = cont =  maisbarato = 0
print("=" * 30)
while True:
    nomeproduto = str(input("Digite o nome do produto: ")).strip()
    preçoproduto = float(input("Digite o preço do produto: R$"))
    esc = str(input("Deseja continuar [S/N]? ")).strip()[0]
    cont += 1
    while esc not in 'SsNn':
        esc = str(input("Opção inválida, digite novamente: "))
    totalcompra += preçoproduto
    if cont == 1:
        maisbarato = preçoproduto
    else:
        if preçoproduto < maisbarato:
            maisbarato = preçoproduto
    if preçoproduto >= 1000:
        produtos1000 += 1
    if esc in 'Nn':
        break
print("=" * 30)
print(f'''O valor total da compra é de R${totalcompra}.
Tem {produtos1000} que custa mais de R$1000.00
O produto mais barato custa R${maisbarato:.2f}''')
