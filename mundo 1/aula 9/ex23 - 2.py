num = int(input("Digite um número: "))
uni = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f"Analisando o número {num}.")
print(f"Unidade: {uni}")
print(f"Dezena: {dez}")
print(f"Centena: {cen}")
print(f"Milhar: {mil}")