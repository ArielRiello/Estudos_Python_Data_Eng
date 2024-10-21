"""
Exercício 3: Leitura e Escrita de Arquivo JSON

    - Crie um programa que leia um arquivo JSON chamado produtos.json, que contém uma lista de produtos com os campos "nome" e "preco".
    - Calcule o total dos preços dos produtos e grave o resultado em um novo arquivo chamado total.json no formato:


Exemplo de entrada (produtos.json):
[
  {"nome": "Produto A", "preco": 10.5},
  {"nome": "Produto B", "preco": 20.0},
  {"nome": "Produto C", "preco": 15.75}
]

O arquivo total.json gerado deve conter:
{
  "total": 46.25
}

"""

import json

def criar_json():
    dados = [
        {"nome": "Produto A", "preco": 10.5},
        {"nome": "Produto B", "preco": 20.0},
        {"nome": "Produto C", "preco": 15.75}
    ]

    arquivo = "produtos.json"

    with open("produtos.json", "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

        print(f"Arquivo {arquivo} criado com sucesso!")

def calcular_total():
    arquivo = "Python/04_Leitura_Escrita_de_Arquivos/produtos.json"

    with open(arquivo, "r") as arquivo_json:
        dados = json.load(arquivo_json)

    valor_total = sum(produto["preco"] for produto in dados)

    with open("total.json", "w") as arquivo_json:
        json.dump({"valor_total": valor_total}, arquivo_json, indent=4)

    print("Arquivo total.json criado com sucesso!")

calcular_total()


"""

json.dump() e json.load(): Funções para salvar e ler dados em formato JSON.

with open(): Usado para abrir arquivos. O bloco with garante que o arquivo seja fechado corretamente.

List comprehension: A expressão sum(produto["preco"] for produto in dados) utiliza uma compreensão de lista para extrair os preços.

Indentação no JSON: O argumento indent=4 torna o JSON mais legível.

json.dump({"valor_total": valor_total}, arquivo_json, indent=4) salva o valor total em um novo arquivo total.json. 
O resultado é armazenado em formato de dicionário para facilitar a leitura do JSON, 
com uma chave "valor_total" associada ao valor calculado.

"""