c1 = c10 = c20 = c50 = total = 0
print("=" * 40)
saque = int(input("Digite o valor do saque: "))
print("=" * 40)
while True:
    if saque >= 50:
        saque -= 50
        c50 += 1
    elif saque >= 20 and saque < 50:
        saque -= 20
        c20 += 1
    elif saque >= 10 and saque < 20:
        saque -= 10
        c10 += 1
    elif saque >= 1 and saque < 10:
        saque -= 1
        c1 += 1
    else:
        break
    total = c1 + c10 + c20 + c50
print("=" * 40)
print(f'''O total de cédulas foi {total}, e será distribuído da seguinte forma:
{c50} cédulas de R$50.00
{c20} cédulas de R$20.00
{c10} cédulas de R$10.00
{c1} moedas de R$1.00''')
print("=" * 40)
