import random

chutes = 0
numero_aleatorio = random.randint(1,101)

while True:
    tentativa = int(input("Digite um número: "))
    chutes += 1
    if tentativa < numero_aleatorio:
        print("Digite um número maior")
    elif tentativa > numero_aleatorio:
        print("Digite um número menor")
    else:
        print("Parabéns você acertou, depois de {} chutes".format(chutes))
        break



    