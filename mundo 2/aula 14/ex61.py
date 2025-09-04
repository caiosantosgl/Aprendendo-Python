t1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite o valor da razão da PA: "))
decimo = t1 + (11 - 1) * razao
cont = 1
while cont <= 10:
    print(t1, end=" --> ")
    t1 += razao
    cont += 1
print("FIM.")