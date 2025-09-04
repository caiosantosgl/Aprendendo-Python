num = int(input("Digite um número inteiro: "))
print('-' * 45)
print("Escolha uma das bases para conversão:")
print("Digite [1] para converter para BINÁRIO.")
print("Digite [2] para converter para OCTAL.")
print("Digite [3] para converter para HEXADECIMAL.")
print('-' * 45)
op = int(input("Sua opção: "))
if op == 1:
    print(f"{num} convertido para BINÁRIO é igual a {bin(num)[2:]}!")
elif op == 2:
    print(f"{num} convertido para OCTAL é igual a {oct(num)[2:]}!")
elif op == 3:
    print(f"{num} convertido para HEXADECIMAL é igual a {hex(num)[2:]}!")
else:
    print("Opção inválida!")