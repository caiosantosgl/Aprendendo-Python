def fatorial(n, show=False):
    """
    > Calcula o Fatorial de um número.
    :param n: O número a ser calculado
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            print(f" x " if c > 1 else " = ", end='')
        fat *= c
    return fat

num = int(input("Digite um valor para ver seu fatorial: "))
print(fatorial(num, show=True))
help(fatorial)
