import math
peso = float(input("Digite seu peso: "))
alt = float(input("Digite sua altura em metros: "))
imc = peso / math.pow(alt, 2)
if imc < 18.5:
    print(f"Seu IMC é {imc:.2f}, você está abaixo do peso ideal.")
    if imc <= 3:
        print("Parabéns, você é uma anomalia!")
elif imc >= 18.5 and imc <= 25:
    print(f"Seu IMC é {imc:.2f}, você está no peso ideal.")
elif imc > 25 and imc < 30:
    print(f"Seu IMC é {imc:.2f}, você está no Sobrepeso!")
elif imc >= 30 and imc < 40:
    print(f"Seu IMC é {imc:.2f}, você está na OBESIDADE!")
else:
    print(f"Seu IMC é {imc:.2f}, você está na OBESIDADE MÓRBIDA!!!")
