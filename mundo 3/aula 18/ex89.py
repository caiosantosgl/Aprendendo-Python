lista =[]
while True:
    nome = str(input('Digite o nome do aluno: '))
    n1 = float(input('Digite a primeira nota: '))
    n2 = float(input('Digite a segunda nota: '))
    med = (n1 + n2) / 2
    lista.append([nome, [n1, n2], med])
    esc = str(input('Deseja continuar [S/N]? '))
    if esc in 'Nn':
        break
print('-=' * 30)
print(f'{"No.":<4}{"Nome":<10}{"Média":>8}')
print('-' * 25)
for a, b in enumerate(lista):
    print(f'{a:<4}{b[0]:<10}{b[2]:>8.1f}')
while True:
    print('-' * 25)
    opç = int(input('Deseja mostrar a nota de qual aluno? (Digite 999 para interromper): '))
    if opç == 999:
        break
    if opç <= len(lista) - 1:
        print(f'As notas do aluno(a) {lista[opç][0]} são: {lista[opç][1]}')
print("FIM...")
