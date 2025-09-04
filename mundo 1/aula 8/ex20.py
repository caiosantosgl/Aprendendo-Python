import random
aln1 = str(input("Digite o nome do primeiro aluno: "))
aln2 = str(input("Digite o nome do segundo segundo: "))
aln3 = str(input("Digite o nome do segundo terceiro: "))
aln4 = str(input("Digite o nome do segundo quarto: "))
lista = [aln1, aln2, aln3, aln4]
random.shuffle(lista)
print(f"A ordem da apresentação será:")
print(lista)