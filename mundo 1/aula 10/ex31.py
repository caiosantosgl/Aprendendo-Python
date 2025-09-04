viagem = int(input("Digite a distância da viagem em KM: "))
if viagem > 0 and viagem <= 200:
    preço1 = viagem * 0.50
    print(f"O custo da viagem é de R${preço1:.2f}!")
else:
    preço2 = viagem * 0.45
    print(f"O custo da viagem é de R${preço2:.2f}!")