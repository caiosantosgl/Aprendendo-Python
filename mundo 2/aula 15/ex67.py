tab = 0
while True:
    val = int(input("Digite um número para ver sua tabuada (de 1 a 10): "))
    print("-" * 15)
    if val < 0:
        break
    for i in range (1, 11):
        res = val * i
        print(f"{val} x {i} = {res}")
    print("-" * 15)
print("FIM")
