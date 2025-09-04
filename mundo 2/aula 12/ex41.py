import datetime
nasc = int(input("Digite seu ano de nascimento: "))
ano = datetime.date.today().year - nasc
print(f"Você tem {ano} anos de idade.")
if ano > 0 and ano <= 9:
    print("Sua categoria é: MIRIM.")
elif ano > 9 and ano <= 14:
    print("Sua categoria é: INFANTIL.")
elif ano > 14 and ano <= 19:
    print("Sua categoria é: JUNIOR.")
elif ano > 19 and ano <= 25:
    print("Sua categoria é: SENIOR.")
else:
    print("Sua categoria é: MASTER.")