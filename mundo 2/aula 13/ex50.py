soma = 0
cont = 0
for val in range(1, 7):
    user = int(input(f"Digite o {val}° valor para fazer a soma: "))
    if user % 2 == 0:
        soma = soma + user
        cont = cont + 1
print(f"Você digitou {cont} número(os) par(es), e a somatoria desse(es) número(os) é: {soma}.")