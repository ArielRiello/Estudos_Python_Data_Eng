"""
Desafio 3: Jogo da Adivinhação

    - Crie um programa que gere um número aleatório entre 1 e 100 (você pode usar uma função de biblioteca como random.randint() para isso).
    - O usuário deve tentar adivinhar o número.
    - Use uma estrutura condicional para verificar se a tentativa do usuário está correta, maior ou menor que o número gerado.
    - O programa deve continuar pedindo tentativas (usando um loop while) até que o usuário adivinhe corretamente.
    - No final, mostre quantas tentativas o usuário precisou para acertar.

"""

import random

numero_secreto = random.randint(1, 100)

tentativas = 0

while True:

    numero_resposta = int(input("Digite um numero inteiro para tentar adivinhar o numero SECRETO!\n"))

    tentativas += 1

    if numero_resposta < numero_secreto:
        print(f"{numero_resposta} é MENOR que o numero SECRETO!")
    elif numero_resposta > numero_secreto:
        print(f"{numero_resposta} é MAIOR que o numero SECRETO!")

    elif numero_resposta == numero_secreto:
        print(f"VOCE ACERTOU !!!")
        print(f"Tentativas: {tentativas}")
        break