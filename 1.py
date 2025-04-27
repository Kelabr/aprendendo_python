# Exercício – Adivinhe o número mágico
# Crie um programa em Python que:

# Escolhe um número secreto entre 1 e 20 (pode ser fixo ou usar import random).

# O usuário tem até 5 tentativas para adivinhar.

# A cada tentativa, o programa:

# Pede ao usuário para digitar um número.

# Informa se o número é maior, menor ou igual ao número secreto.

# Se o usuário acertar, o programa exibe: "Parabéns! Você acertou!"

# Se errar todas, exibe: "Suas tentativas acabaram! O número era X."


import random

numero_secreto = random.randint(1,20)
tentativas = 0

while tentativas < 5:
    numero = int(input("Escolha um número entre '1' e '20': "))
    tentativas += 1

    if numero == numero_secreto:
        print("ACERTOUUU!!!")
        break
    else:
        print(f"Errou, você tem {5 - tentativas} tentativas sobrando ")

if numero != numero_secreto:
    print(f"Suas tentativas foram esgotadas - O número secreto é {numero_secreto}")





