num = []
maiorV = 0
menorV = 0
for v in range(0, 5):
    num.append(int(input(f"Digite um valor para posição {v}: ")))
    if v == 0:
        maiorV = menorV = num[v]
    else:
        if num[v] > maiorV:
            maiorV = num[v]
        if num[v] < menorV:
            menorV = num[v]
print(f"Os valores digitados foram: {num}")
print(f"O maior valor digitado foi: {maiorV}")
print(f"O menor valor digitado foi: {menorV}")
print(f"O maior valor foi digitado nas posições: ", end='')
for p, c in enumerate(num):
    if c == maiorV:
        print(p, end=' ')
print()
print(f"O menor valor foi digitado nas posições: ", end='')
for p, c in enumerate(num):
    if c == menorV:
        print(p, end=' ')
