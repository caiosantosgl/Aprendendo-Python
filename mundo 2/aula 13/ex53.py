frase = str(input("Digite a sua frase: ")).strip().upper()
palavras = frase.split()
juntar = ''.join(palavras)
inversofrase = ''
for l in range(len(juntar) -1, -1, -1):
    inversofrase += juntar[l]
print(f"O inverso de {juntar} é {inversofrase}")
if inversofrase == juntar:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo!")
