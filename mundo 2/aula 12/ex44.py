print("----------------------------------------- LOJA -----------------------------------------")
preço = float(input("Digite o preço das compras: R$"))
print("Formas de pagamento:")
print("Digite [1] para pagamento à vista dinheiro/cheque.")
print("Digite [2] para pagamento à vista cartão.")
print("Digite [3] para pagamento parcelado 2x no cartão.")
print("Digite [4] para pagamento parcelado 3x ou mais no cartão.")
opç = int(input("Qual a opção de pagamento? "))
if opç == 1:
    preçototal = preço - (preço * 10/100)
    print(f"No pagamento à vista (dinheiro/cheque) você recebe um desconto de 10%, o preço final é de: R${preçototal:.2f}!")
elif opç == 2:
    preçototal = preço - (preço * 5/100)
    print(f"No pagamento à vista no cartão, você recebe um desconto de 10%, o preço final é de: R${preçototal:.2f}!")
elif opç == 3:
    preçototal = preço
    parcela = preçototal / 2
    print(f"Serão 2 parcelas de R${parcela:.2f} no cartão!")
elif opç == 4:
    preçototal = preço + (preço * 20/100)
    qntparcelas = int(input("Digite a quantidade de parcelas: "))
    calcparcelas = preçototal / qntparcelas
    print(f"Serão divididas em {qntparcelas} de R${calcparcelas:.2f} (parcelado em 3x ou mais, é cobrado uma taxa de 20% de juros).")
else:
    preçototal = preço
    print("Opção de pagamento inválida!")
print(f"Sua compra de R${preço:.2f} vai ficar no valor final por: R${preçototal:.2f}!")
