from datetime import date
def voto(ano):
    anoatual = date.today().year
    idade = anoatual - ano
    if idade > 0 and idade < 16:
        return f'Não pode votar com {idade} anos de idade.'
    elif idade >= 16 and idade <= 18 or idade > 65:
        return f'Com {idade} anos o voto é opcional.'
    else:
        return f'Com {idade} anos de idade, o voto é obrigatório.'
    
n = int(input("Digite o seu ano de nascimento: "))
print(voto(n))