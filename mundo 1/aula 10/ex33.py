n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
n3 = int(input("Digite o terceiro valor: "))
#menor valor
if n1 < n2 and n1 < n3:
    print(f"O menor valor é {n1}.")
if n2 < n1 and n2 < n3:
    print(f"O menor valor é {n2}.")
if n3 < n1 and n3 < n2:
    print(f"O menor valor é {n3}.")
#menor valor

if n1 > n2 and n1 > n3:
    print(f"O maior valor é {n1}.")
if n2 > n1 and n2 > n3:
    print(f"O maior valor é {n2}.")
if n3 > n1 and n3 > n2:
    print(f"O maior valor é {n3}.")