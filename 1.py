#Código feito por mim 

# import random

# numero_secreto = random.randint(1, 20)
# acertou = False
# tentativas = 0
# numero = int(input("Digite um número entre '1' e '20': "))


# while acertou == False and tentativas < 4 :
#     if numero != numero_secreto:
#         print("Iiiii ERROU EMMM")
#         tentativas += 1
#         print(tentativas)
#         print(numero)
#         print(numero_secreto)
#         numero = int(input("Digite um número entre '1' e '20': "))
#     else:
#         print("Acertouuu")
#         acertou = True
#         break


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





