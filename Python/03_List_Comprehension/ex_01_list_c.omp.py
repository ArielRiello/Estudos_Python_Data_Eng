"""
Exercício 1: Filtrar e transformar números

    - Dada uma lista de números inteiros, crie uma nova lista que contenha o quadrado de cada número, mas apenas para os números que são pares.
    - Exemplo de entrada: [1, 2, 3, 4, 5, 6]
    - Exemplo de saída esperada: [4, 16, 36]

"""

lista = [1, 2, 3, 4, 5, 6]

lista_pares = [x for x in lista if x % 2 == 0]

lista_impares = [x for x in lista if x % 2 != 0]

print("Pares: ",lista_pares)
print("Impares: ",lista_impares)