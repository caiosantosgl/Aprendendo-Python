vel = int(input("Qual a velocidade do carro? "))
if vel > 80:
    print("Você foi multado por exceder o limite de velocidade!")
    multa = (vel-80) * 7
    print(f"O valor da multa a pagar é de R${multa:.2f}!")
print("Diraja com responsabilidade.")