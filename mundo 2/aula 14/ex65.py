somatoriamedia = 0
divisormedia = 0
cont = 0
maiornum = 0
menornum = 0
fim = ''
while fim in 'Ss':
    n = int(input("Digite um número: "))
    somatoriamedia += n
    divisormedia += 1
    cont += 1
    fim = str(input("Deseja continuar? [S/N]: ")).strip()[0]
    if cont == 1:
        maiornum = menornum = n
    else:
        if n > maiornum:
            maiornum = n
        if n < menornum:
            menornum = n
media = somatoriamedia / divisormedia
print(f"O maior número é {maiornum}, o menor número é {menornum}, e a média entre todos os valores é: {media}.")
