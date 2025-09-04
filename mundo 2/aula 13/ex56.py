maiorH = 0
mediaidd = 0
somaidd = 0
nomeV = ''
mulher20 = 0
for c in range(1, 5):
    print("-" * 8, f"{c}° Pessoa","-" * 8)
    nome = str(input('Digite seu Nome: ')).strip()
    idade = int(input("Digite sua Idade: "))
    sexo = str(input("Digite seu Sexo [M/F]: ")).strip()
    somaidd += idade
    if c == 1 and sexo in 'Mm':
        maiorH = idade
        nomeV = nome
    if sexo in 'Mm' and idade > maiorH:
        maiorH = idade
        nomeV = nome
    if sexo in 'Ff' and idade < 20:
        mulher20 += 1
mediaidd = somaidd / 4
print(f"A média de idade dessas pessoas é: {mediaidd}.")
print(f"O homem mais velho tem {maiorH} anos e se chama {nomeV}.")
print(f"Tem {mulher20} mulheres com menos de 20 anos.")
