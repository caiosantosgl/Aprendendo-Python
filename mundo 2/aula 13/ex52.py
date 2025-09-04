val = int(input("Digite um número: "))
cont = 0
for i in range(1, val + 1):
    if val % i == 0:
        print(f"{val} é divisível por {i}.", end=" - ")
        cont += 1
    else:
        print(f"{val} é não divisível por {i}.", end=" - ")
print("Fim.")
print('-=-' * 10)
print(f"O número {val} foi dividido {cont} vezes.")
if cont == 2:
    print(f"O número {val} é primo!")
else:
    print(f"O número {val} não é primo!")
