# Caixa eletrónico 

# Desafio – Caixa eletrônico
# Faça um programa em Python que simula o funcionamento de um caixa eletrônico.

# Regras:

# O programa deve pedir para o usuário informar um valor para sacar (apenas números inteiros positivos).

# O programa deve calcular quantas notas de cada valor serão entregues. Considere que o caixa tem apenas notas de: 100, 50, 20, 10, 5 e 1 reais.

# Mostrar no final:

# Quantas notas de cada tipo foram entregues (apenas se for usado).

Saque = int(input("Quanto você quer sacar?"))

def escolha_notas(saque):
    cedulas = [100, 50, 20, 10, 5, 1]

    for nota in cedulas:
        if saque // nota != 0 :
            print(f"O cliente receberá {saque // nota} da cedula de {nota}")
            saque = saque - ((saque // nota) * nota) 



escolha_notas(Saque)











