"""
Exercício com Conjuntos

Dado dois conjuntos de números inteiros:

    - Conjunto A: {1, 2, 3, 4, 5}
    - Conjunto B: {4, 5, 6, 7, 8}

Realize as seguintes operações:

    - Calcule e exiba a união dos conjuntos.
    - Calcule e exiba a interseção dos conjuntos.
    - Calcule e exiba a diferença de A para B.

"""

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

uniao = conjunto_a | conjunto_b
print("União Conjunto A com Conjunto B: ",uniao)

intersecao = conjunto_a & conjunto_b
print("Interseção Conjunto A com Conjunto B: ", intersecao)

diferenca = conjunto_a - conjunto_b
print("Diferença Conjunto A com Conjunto B: ", diferenca)

# OBS:

# A união resulta em um conjunto contendo todos os elementos de conjunto_a e conjunto_b, sem duplicação.

# A interseção resulta em um conjunto contendo apenas os elementos que estão presentes em ambos os conjuntos.

# A diferença entre conjunto_a e conjunto_b resulta em um conjunto contendo os elementos que estão em conjunto_a, mas não em conjunto_b.