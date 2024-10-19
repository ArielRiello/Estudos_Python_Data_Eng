"""
Exercício 1: Leitura e Escrita de Arquivo de Texto

    - Crie um programa que leia o conteúdo de um arquivo de texto chamado entrada.txt e conte quantas palavras existem no arquivo.
    - Em seguida, grave o resultado (número de palavras) em um novo arquivo chamado saida.txt.
    - Exemplo: Se o conteúdo de entrada.txt for "Olá, mundo! Python é incrível.", o arquivo saida.txt deve conter "Número de palavras: 5".

"""

def criar_arquivo():

    novo_arquivo = open("arquivo_entrada.txt",'w')

    conteudo = "Olá, mundo! Python é incrível."

    novo_arquivo.write(conteudo)

    novo_arquivo.close()

criar_arquivo()

local_arquivo = "arquivo_entrada.txt"

with open(local_arquivo, "r") as arquivo:
    conteudo = arquivo.read()

quantidade_caracteres = len(conteudo)
print("Quantidade caracteres: ", quantidade_caracteres)
    
quantidade_letras = len([char for char in conteudo if char.isalpha()])
print("Quantidade letras: ", quantidade_letras)

quantidade_palavras = conteudo.split()
print("Quantidade de palavras: ", len(quantidade_palavras))


# OBS:

# 'with' é usado para gerenciar o contexto de abertura de arquivos, garantindo que eles sejam fechados corretamente.

# 'split()' divide uma string em uma lista de substrings com base em um delimitador (por padrão, espaços em branco).

# 'len()' retorna o número de elementos em uma sequência, como o número de caracteres em uma string ou itens em uma lista.

# 'isalpha()' verifica se todos os caracteres de uma string são letras do alfabeto, retornando True ou False.