sal = float(input("Digite o valor do salário: R$"))
a10 = sal + (sal*10/100)
a15 = sal + (sal*15/100)
if sal > 0 and sal <= 1250.00:
    print(f"O novo valor do salário com aumento é: R${a15:.2f}!")
else:
    print(f"O novo valor do salário com aumento é: R${a10:.2f}!")