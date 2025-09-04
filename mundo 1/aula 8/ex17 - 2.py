import math
cop = float(input("Digite o valor do cateto oposto: "))
cad = float(input("Digite o valor do cateto adjacente: "))
hip = math.hypot(cop, cad)
print(f"A hipotenusa mede {hip}.")