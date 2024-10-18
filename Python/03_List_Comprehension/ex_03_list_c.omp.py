"""
3. Exercício 3: Combinações de listas

    - Crie uma lista de tuplas que represente todas as combinações possíveis entre dois conjuntos de números.
    - Dadas duas listas de números, [1, 2, 3] e [4, 5, 6], gere uma lista de pares (x, y) onde x vem da primeira lista e y da segunda.
    - Exemplo de saída esperada: [(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]

""" 

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]

combinacao = [(a, b) for a in lista_a for b in lista_b]

print(combinacao)