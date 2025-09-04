user = int(input("Digite um valor para ver a sua tabuada: "))
cont = 0
print("-=-" * 15)
for i in range(1, 11):
    cont = cont + 1
    tab = user * cont
    print(f"[ {user} ] X [ {cont} ] = {tab}.")
print("-=-" * 15)