import datetime
nasc = int(input("Digite seu ano de nascimento: "))
atual = datetime.date.today().year
Ida = atual - nasc
print(f"Quem nasceu em {nasc} tem {Ida} anos em {atual}.")
if Ida == 18:
    print("Você deve se alistar!")
elif Ida > 18:
    temp = Ida - 18
    ano = atual - temp
    print("Você já deveria ter se alistado!")
    print(f"Seu ano de alistamento foi em {ano}")
elif Ida < 18:
    temp = 18 - Ida
    print(f"Ainda faltam {temp} para você se alistar, seu alistamento será em {atual + temp}!")