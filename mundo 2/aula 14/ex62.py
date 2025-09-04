t1 = int(input("Digite o primeiro termo da PA: "))
razao = int(input("Digite o valor da razão da PA: "))
t = t1
tmais = 10
cont = 1
cont2 = 0
while tmais != 0:
    cont2 = cont2 + tmais
    while cont <= cont2:
        print(t, end=" --> ")
        t += razao
        cont += 1
    print("...")
    tmais = int(input("Digite quantos termos a mais você quer: "))
print(f"A progressão foi finalizada com {cont2} termos mostrados.")