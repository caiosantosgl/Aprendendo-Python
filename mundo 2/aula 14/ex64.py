cont = 0
soma = 0
n = int(input("Digite um número inteiro (ou 999 para parar): "))
while n != 999:
    cont += 1
    soma += n
    n = int(input("Digite um número inteiro (ou 999 para parar): "))
print(f"A quantidade de números digitados foi {cont} e a soma de todos os números é: {soma}.")
