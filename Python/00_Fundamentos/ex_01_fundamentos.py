"""
Calculadora de Descontos

    - Crie um programa que pergunte ao usuário o valor original de um produto e a porcentagem de desconto.
    - Use operadores para calcular o valor com desconto.
    - Utilize uma estrutura condicional para garantir que a porcentagem de desconto esteja entre 0 e 100. Caso contrário, exiba uma mensagem de erro.
    - Use um loop while para permitir que o usuário calcule o desconto de vários produtos até que ele decida parar (usando uma palavra-chave como "sair").

"""

class VerificarPorcentagem(Exception):
    pass

def verificar_porcentagem_negativo(porcentagem):
    if porcentagem > 100:
        raise VerificarPorcentagem("A porcentagem de desconto não pode passar de 100%")
    elif porcentagem <= 0:
        raise VerificarPorcentagem("Zero ou menos não resultaram em nenhum desconto")

def calcular_desconto(valor, porcentagem):
    valor_desconto = valor * (porcentagem / 100)

    return valor_desconto

while True:
    try:
        print("\nCALCULADORA DE DESCONTOS\n")
        valor = float(input("Informe o valor do item: "))
        desconto = int(input("\nInforme a porcentagem do desconto: "))

        verificar_porcentagem_negativo(desconto)

        valor_desconto_final = calcular_desconto(valor, desconto)

        print(f"\n{desconto}% de {valor:.2f}, o valor do desconto será: R$ {valor_desconto_final:.2f}")

        novo_sair = ""

        while novo_sair not in ["NOVO", "SAIR"]:
            novo_sair = input("""\nDigite "SAIR" para sair\nDigite "NOVO" para calcular um novo desconto\n""").upper()

        if novo_sair == "NOVO":
            continue
        elif novo_sair == "SAIR":
            break

    except VerificarPorcentagem as e:
        print(f"Erro: {e}")
        continue