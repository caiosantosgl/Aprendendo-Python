n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
med = (n1 + n2) / 2
print(f"A média do aluno é {med}.")
if med >= 0 and med < 5:
    print("Reprovado!")
elif med >= 5 and med <= 6.9:
    print("Recuperação!")
elif med >= 7 and med <= 10:
    print("Aprovado!")
else:
    print("Nota inválida!")