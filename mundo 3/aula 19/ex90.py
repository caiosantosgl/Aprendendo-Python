alunos = {}
alunos['nome'] = str(input("Digite o nome do aluno: "))
alunos['media'] = float(input("Digite a média do aluno: "))
print(f"O nome do aluno é: {alunos['nome']}")
print(f"A média do aluno é: {alunos['media']}")
situaçao = {'Reprovado': 'Reprovado', 'Aprovado': 'Aprovado'}
if alunos['media'] >= 0 and alunos['media'] < 6:
    print(f"A situação do aluno é: {situaçao['Reprovado']}.")
elif alunos['media'] >= 6 and alunos['media'] <= 10:
    print(f"A situação do aluno é: {situaçao['Aprovado']}")
