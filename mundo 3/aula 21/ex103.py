def ficha(nome='<Não informado/desconhecido.>', gols=0):
    print(f"O jogador {nome} fez {gols} gols.")

nm = str(input("Digite o nome do jogador: "))
gl = str(input("Digite a quantidade de gols: "))
if gl.isnumeric():
    gl = int(gl)
else:
    gl = 0
if nm.strip() == '':
    ficha(gols=gl)
else:
    ficha(nm, gl)
