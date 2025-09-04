import math
ang = int(input("Digite o valor de um ângulo notável: "))
seno = math.sin(math.radians(ang))
cosseno = math.cos(math.radians(ang))
tangente = math.tan(math.radians(ang))
print(f"O seno de {ang} é  {seno:.2f}")
print(f"O cosseno de {ang} é  {cosseno:.2f}")
print(f"A tangente de {ang} é  {tangente:.2f}")