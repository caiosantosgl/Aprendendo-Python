import datetime
anoatual = datetime.date.today().year
contmaior = 0
contmenor = 0
for i in range(1, 8):
    pessoa = int(input(f"Digite o ano de nascimento da {i}° pessoa: "))
    calcidade = anoatual - pessoa
    if calcidade >= 18:
        contmaior += 1
    elif calcidade >= 0 and calcidade < 18:
        contmenor += 1
    else:
        print("Ano de nascimento ou idade inválida!")
print(f"O total de pessoas maiores de idade é: {contmaior}.")
print(f"O total de pessoas menor de idade é: {contmenor}.")
