"""
2. Exercício 2: Palavras com letras específicas

    - Dada uma lista de palavras, crie uma nova lista contendo apenas as palavras que começam com a letra "a" ou "e".
    - Exemplo de entrada: ["apple", "banana", "avocado", "grape", "elderberry", "orange"]
    - Exemplo de saída esperada: ["apple", "avocado", "elderberry"]

"""

lista = ["apple", "banana", "avocado", "grape", "elderberry", "orange"]

palavras_a_e = [l for l in lista if l[0] == "a" or l[0] == "e"]

print(palavras_a_e)