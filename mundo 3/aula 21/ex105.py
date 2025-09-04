def notas(*n, sit=False):
    """
    > Analisa notas e as situações dos alunos.
    parâmetro "n": notas dos alunos (aceita várias).
    parâmetro "sit": valor opcional, indicando a situação do aluno.
    return: dicionário com as informações sobre os alunos.
    """
    b = {}
    b['total'] = len(n)
    b['maior'] = max(n)
    b['menor'] = min(n)
    b['média'] = sum(n)/len(n)
    if sit:
        if b['média'] >= 6:
            b['situação'] = 'boa'
        elif b['média'] >= 4:
            b['situação'] = 'Ainda da pra salvar'
        elif b['média'] >= 0 and b['média'] < 4:
            b['média'] = 'Se lascou'
    return b

a = notas(5.5, 2.5, 9, 8.5, sit=True)
print(a)
help(notas)