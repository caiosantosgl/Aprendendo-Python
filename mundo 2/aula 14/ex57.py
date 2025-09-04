sexo = str(input("Digite seu Sexo [M/F]: ")).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input("Digite novamente: ")).strip().upper()[0]
print("Fim.")
