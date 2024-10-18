"""
Exercício com Lista

Crie uma lista com 10 números inteiros. Em seguida:

    - Calcule e exiba a soma de todos os elementos da lista.
    - Remova o maior e o menor valor da lista.
    - Imprima a lista resultante.

"""

import random

lista = []

for i in range(0, 10):
    lista.append(random.randint(0, 10))
    print(lista)

lista.sort()
print("Lista ordenada:", lista)

lista.pop()
print("Após remover o último:", lista)

lista.pop(0)
print("Após remover o primeiro:", lista)