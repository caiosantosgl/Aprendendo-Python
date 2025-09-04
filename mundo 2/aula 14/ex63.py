print("-" * 5, "Sequência de Fibonacci", "-" * 5)
quantidadetermo = int(input("Digite a quantidade de termos que você quer mostrar: "))
t1 = 0
t2 = 1
cont = 3
print(f"{t1} --> {t2}", end=" ")
while cont <= quantidadetermo:
    t3 = t1 + t2
    print(f" --> {t3}", end=" " )
    cont += 1
    t1 = t2
    t2 = t3
print('FIM')
