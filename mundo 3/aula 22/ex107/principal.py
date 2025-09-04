import moeda
preço = float(input("Digite o preço: R$"))
print(f"A metade do valor R${preço} é R${moeda.metade(preço)}")
print(f"O dobro do valor R${preço} é R${moeda.dobro(preço)}")
print(f"Aumentando o valor do preço em 10%, temos R${moeda.aumentar(preço, 10)}")
print(f"Diminuindo o valor do preço em 10%, temos R${moeda.diminuir(preço, 10)}")
