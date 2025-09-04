quantidadenum = somatoria = 0
while True:
    n = int(input("Digite um número (ou 999 para parar): "))
    if n == 999:
        break
    quantidadenum += 1
    somatoria += n
print(f"O total de números digitados é: {quantidadenum}, e a somatoria entre eles é: {somatoria}.")
