maiorp = 0
menorp = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}° pessoa: "))
    if i == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        if peso < menorp:
            menorp = peso
print(f"O maior peso em KG foi de {maiorp}.")
print(f"O menor peso em KG foi de {menorp}.")
