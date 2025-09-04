import moeda2
preço = float(input("Digite o preço: R$"))
print(f"A metade do valor {moeda2.moeda(preço, "US$")} é {moeda2.moeda(moeda2.metade(preço))}")
print(f"O dobro do valor {moeda2.moeda(preço)} é {moeda2.moeda(moeda2.dobro(preço))}")
print(f"Aumentando o valor do preço em 10%, temos {moeda2.moeda(moeda2.aumentar(preço, 10))}")
print(f"Diminuindo o valor do preço em 10%, temos {moeda2.moeda(moeda2.diminuir(preço, 10))}")
