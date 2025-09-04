def dobro(preço=0, formatado=False):
    res = preço * 2
    return res if formatado is False else moeda(res)

def diminuir(preço=0, taxa=0, formatado=False):
    res = preço - (preço * taxa/100)
    return res if formatado is False else moeda(res)

def aumentar(preço=0, taxa=0, formatado=False):
    res = preço + (preço * taxa/100)
    return res if formatado is False else moeda(res)

def metade(preço=0, formatado=False):
    res = preço / 2
    return res if formatado is False else moeda(res)

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>8.2f}'.replace('.', ',')

def resumo(preço=0, taxaau=10, taxad=10):
    print("=" * 50)
    print("SIMPLIFICADO".center(50))
    print("=" * 50)
    print(f"Analisando preço: {moeda(preço)}")
    print(f"Metade do preço: {metade(preço, True)}")
    print(f"Dobro do preço: {dobro(preço, True)}")
    print(f"Com {taxaau}% de aumento: {aumentar(preço, taxaau, True)}")
    print(f"Com {taxad}% de diminuição: {diminuir(preço, taxad, True)}")
    print('=' * 50)