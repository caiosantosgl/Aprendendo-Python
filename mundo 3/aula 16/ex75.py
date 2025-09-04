n = (int(input('Dig. um núm: ')), 
     int(input('Dig. outro núm: ')),
     int(input('Dig. mais um núm: ')),
     int(input('Dig. o último núm: ')))
print(f"Você digitou os valores {n}")
print(f"O valor 9 apareceu {n.count(9)} vezes.")
if 3 in n:
    print(f"O valor 3 apareceu na {n.index(3)+1}° posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")
print("Os valores pares digitados foram: ", end="")
for a in n:
    if a % 2 == 0:
        print(a, end='')
        