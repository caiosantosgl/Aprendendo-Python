import moeda3
preço = float(input("Digite o preço: R$"))
print(f"A metade do valor {moeda3.moeda(preço,)} é {moeda3.metade(preço, True)}")
print(f"O dobro do valor {moeda3.moeda(preço)} é {moeda3.dobro(preço, True)}")
print(f"Aumentando o valor do preço em 10%, temos {moeda3.aumentar(preço, 10, True)}")
print(f"Diminuindo o valor do preço em 10%, temos {moeda3.diminuir(preço, 10, True)}")
