cs = float(input("Digite o valor da casa: R$"))
sa = float(input("Digite o valor do seu salário: R$"))
an = int(input("Digite o tempo (em anos) do financiamento: "))
pres = cs / (an * 12)
mini = sa * 30/100
if pres <= mini:
    print("O emprestimo pode ser feito.")
else:
    print("Emprestimo negado!")