kmrodados = float(input("Quantos KM foram rodados? "))
dias = int(input("Quantos dias alugados? "))
pag = (dias * 60) + (kmrodados * 0.15)
print(f"O total a pagar é R${pag}.")