def leitaInt(m):
    a = False
    val = 0
    while True:
        v = str(input(m))
        if v.isnumeric():
            val = int(v)
            a = True
        else:
            print("ERRO! Digite um valor inteiro válido.")
        if a:
            break
    return val

v = leitaInt('Digite um valor: ')
print(f"Você digitou o valor {v}.")
