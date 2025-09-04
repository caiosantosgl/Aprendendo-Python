from time import sleep
def maior(* val):
    cont = maior = 0
    print(f"=" * 30)
    for v in val:
        print(f"{v} ", end="", flush=True)
        sleep(0.5)
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f"{cont} valores foram digitados ao todo.")
    print(f"O maior valor é {maior}.")

maior(2, 5, 8, 6, 7, 46, 1321, 63320, 645, 46, 5, 645)
maior(1, 3, 5, 7, 9, 11)
maior(0, 2, 4, 8)
maior(-1, 2)
maior(10)
maior()
