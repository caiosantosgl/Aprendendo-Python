termo1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite o valor da razão da PA: "))
termo10 = termo1 + (11 - 1) * razao
for c in range(termo1, termo10, razao):
    print(f"{c}", end=" --> ")
print("FIM.")