"""
Exercício 2: Manipulação de Arquivo CSV

    - Crie um programa que leia um arquivo CSV chamado pessoas.csv, que contém uma lista de pessoas com os campos "Nome" e "Idade".
    - Filtre as pessoas que têm idade maior ou igual a 18 e salve essas informações em um novo arquivo chamado maiores_de_idade.csv.

"""

import csv

def criar_arquivo():
    dados = [
        ["Nome", "Idade"],
        ["Ariel", 32],
        ["João", 16],
        ["Ana", 18],
        ["Carlos", 17],
    ]

    nome_arquivo = "dados.csv"

    with open(nome_arquivo, mode="w", newline="") as arquivo_csv:
        escritor = csv.writer(arquivo_csv)
        escritor.writerows(dados)

    print(f"Arquivo {nome_arquivo} criado com sucesso!")



def ler_arquivo(local_arquivo):
    with open(local_arquivo, "r") as arquivo:
        
        conteudo = arquivo.read()
        
        print(conteudo)


def filtrar_maior_idade(local_arquivo):
    maiores = []

    with open(local_aquivo, "r") as arquivo:
        leitor = csv.reader(arquivo)
        next(leitor)

        for linha in leitor:
            nome, idade = linha
            if int(idade) >= 18:
                maiores.append([nome, idade])

        print(maiores)


local_aquivo = "Python/04_Leitura_Escrita_de_Arquivos/dados.csv"

criar_arquivo(local_aquivo)

ler_arquivo(local_aquivo)

filtrar_maior_idade(local_aquivo)


"""
OBS:

csv: Biblioteca padrão do Python para manipulação de arquivos CSV (Comma-Separated Values).
Ela permite a leitura e escrita de arquivos em formato de tabela, onde cada linha é uma entrada 
e os campos são separados por vírgulas.

O parâmetro newline="" é usado para evitar linhas em branco adicionais ao escrever no CSV no Windows

A função csv.writer() cria um objeto que permite escrever dados em formato CSV no arquivo.

O método writerows(dados) escreve todas as linhas da lista dados no arquivo.

leitor = csv.reader(arquivo) cria um objeto csv.reader, que é usado para ler o conteúdo do arquivo CSV linha por linha.

O csv.reader interpreta cada linha do arquivo como uma lista de strings, separando os valores de acordo com as vírgulas.

next(leitor) avança para a próxima linha do objeto leitor, ignorando a primeira linha, 
que geralmente é o cabeçalho (neste caso, "Nome" e "Idade"). 
Isso evita que o cabeçalho seja processado como parte dos dados.

"""