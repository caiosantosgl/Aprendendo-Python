import datetime
info = {}
info['nome'] = str(input("Digite seu nome: "))
nasc = int(input("Digite seu nome de nascimento: "))
clt = int(input("Carteira de trabalho (0 não tem): "))
info['idade'] = datetime.date.today().year - nasc
info['ctps'] = clt
if info['ctps'] != 0:
    info['contrato'] = int(input("Digite o ano de contratação: "))
    info['salario'] = float(input("Digite o valor do seu salário: R$"))
    info['aposenta'] = info['idade'] + (info['contrato'] + 35) - datetime.date.today().year
for c, v in info.items():
    print(f"{c} tem o valor {v}")
