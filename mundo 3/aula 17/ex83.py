exp = str(input("Digite sua expressão: "))
note = []
for p in exp:
    if p == '(':
        note.append('(')
    elif p == ')':
        if len(note) > 0:
            note.pop()
        else:
            note.append(')')
            break
if len(note) == 0:
    print("Está expressão é válida!")
else:
    print("Sua expressão está incorreta!")
