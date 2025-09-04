v1 = int(input("Digite um valor: "))
v2 = int(input("Digite outro valor: "))
esc = 0
while esc != 5:
    print("""Escolha uma das opções:
    [1] - Soma
    [2] - Multiplicar
    [3] - Maior
    [4] - Novos Números
    [5] - Sair do programa""")
    esc = int(input("Digite sua opção: "))
    if esc == 1:
        soma = v1 + v2
        print(f"[{v1}] + [{v2}] = {soma}")
    elif esc == 2:
        mult = v1 * v2
        print(f"[{v1}] x [{v2}] = {mult}")
    elif esc == 3:
        if v1 > v2:
            print(f"O primeiro número {v1} é maior.")
        elif v2 > v1:
            print(f"O segundo número {v2} é maior.")
        else:
            print("Os valores são iguais.")
    elif esc == 4:
        print("Digite os números novamente.")
        v1 = int(input("Digite um valor: "))
        v2 = int(input("Digite outro valor: "))
    elif esc == 5:
        print("Encerrando...")        
    else:
        print("Escolha inválida, tente novamente!")
print("Fim.")
