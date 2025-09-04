import time
print('-=-' * 10, "A contagem para os fogos vai começar!", '-=-' * 10)
for c in range(10, -1, -1):
    print(f"Contagem regressiva: {c}!")
    time.sleep(1)
print("Fim da contagem.")
print("-=-" * 15)