l1 = int(input("Digite o valor do primeiro segmento: "))
l2 = int(input("Digite o valor do segundo segmento: "))
l3 = int(input("Digite o valor do terceiro segmento: "))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print("Os segmentos acima podem formar um triângulo.", end='')
    if l1 == l2 and l2 == l3:
        print("O triângulo é EQUILÁTERO.")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        print("O triângulo é ESCALENO.")
    else:
        print("O triângulo é ISÓCELES.")
else:
    print("Os segmentos acima não podem formar um triângulo.")