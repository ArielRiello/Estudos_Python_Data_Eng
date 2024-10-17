"""
Exercício 3: Conversão de Temperatura

    - Crie uma função chamada converter_temperatura que recebe dois parâmetros: a temperatura e a unidade de conversão desejada ("C" para Celsius ou "F" para Fahrenheit).
    
    - Se a unidade for "C", a função deve converter a temperatura de Fahrenheit para Celsius.
    
    - Se a unidade for "F", a função deve converter a temperatura de Celsius para Fahrenheit.
    
    - A função deve retornar o valor convertido e a unidade de destino.
    
    - Teste a função com diferentes valores e unidades.

"""

def celsius_para_fahrenheit(celsius):
    fahrenheit = celsius * (9/5) + 32
    return fahrenheit

def fahrenheit_para_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

temperatura_unidade = input(
    "Digite uma temperatura seguida de uma unidade para convertê-la:\n"
    "Exemplo: '100 C' para Celsius ou '212 F' para Fahrenheit.\n"
).upper()

temperatura, unidade = temperatura_unidade.split()

temperatura = float(temperatura)

if unidade == "C":
    conversao = fahrenheit_para_celsius(temperatura)
    print(f"{temperatura} graus Celsius = {conversao} graus Fahrenheit")
elif unidade == "F":
    conversao = celsius_para_fahrenheit(temperatura)
    print(f"{temperatura} graus Fahrenheit = {conversao} graus Celsius")
else:
     print("Comando inválido! Por favor, use 'C' para Celsius ou 'F' para Fahrenheit.")


# OBS: split() divide a string em uma lista de partes usando o espaço como delimitador.