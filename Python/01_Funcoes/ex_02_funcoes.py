"""
Exercício 2: Verificador de Palíndromo

    - Crie uma função chamada eh_palindromo que recebe uma string como parâmetro.
    
    - A função deve retornar True se a string for um palíndromo (lê-se igual de trás para frente) e False caso contrário.
    
    - Faça uma outra função que pergunte ao usuário uma palavra e use a função eh_palindromo para verificar se é um palíndromo, imprimindo o resultado.

"""


def eh_polindromo(palavra):
    palavra_dividida = []

    for letra in palavra:
        palavra_dividida.append(letra)

    if palavra == "".join(palavra_dividida[::-1]):
        return "É POLINDROMO"
    else:
        return "NÃO É POLINDROMO"

palavra = input("Digite uma palavra: ")
resultado = eh_polindromo(palavra)
print(resultado)


"""
OBS: 

Inversão usando slicing [::-1]: palavra_dividida[::-1] cria uma versão invertida da lista.

Uso de "".join(): A função join() é usada para unir os caracteres de palavra_dividida em uma string, 
tornando possível a comparação com a string original palavra.

"""