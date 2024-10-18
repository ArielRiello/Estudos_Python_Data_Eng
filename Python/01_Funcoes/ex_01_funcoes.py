"""
Exercício 1: Calculadora Simples

    - Crie uma função chamada calculadora que recebe três parâmetros: dois números e uma operação (+, -, *, /).
    - A função deve retornar o resultado da operação com os dois números.
    - Caso a operação não seja válida, retorne uma mensagem de erro.
    - Teste a função com diferentes operações.

"""

def calcular(numero_01, numero_02, operador):

    if operador == "+":
        return numero_01 + numero_02
    elif operador == "-":
        return numero_01 - numero_02
    elif operador == "*":
        return numero_01 * numero_02
    elif operador == "/":
        if numero_02 == 0:
            return "Erro: Divisão por zero não é permitida."
        return numero_01 / numero_02
    else:
        return "Operador inválido!"

print(calcular(3, 5, "*"))
print(calcular(10, 0, "/"))
print(calcular(10, 2, "+"))
print(calcular(7, 3, "-"))
print(calcular(4, 5, "%"))