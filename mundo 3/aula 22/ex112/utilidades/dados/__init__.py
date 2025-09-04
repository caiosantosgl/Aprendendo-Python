def leiaDinheiro(msg):
    vali = False
    while not vali:
        ent = str(input(msg)).replace(',', '.')
        if ent.isalpha() or ent.strip() == '':
            print(f"ERRO! \'{ent}\' é um preço inválido!")
        else:
            vali = True
            return float(ent)
        