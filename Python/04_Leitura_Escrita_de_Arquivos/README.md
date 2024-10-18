
# Leitura e Escrita de Arquivos em Python

- Em Python, a manipulação de arquivos é feita usando funções como `open()`, `read()`, `write()`, e o uso do bloco `with` para gerenciar os arquivos de forma segura. Também é comum trabalhar com formatos específicos, como **CSV** e **JSON**, que são amplamente usados para armazenar e trocar dados.

---

### Manipulação de Arquivos com `open()`, `read()`, `write()`, e `with`

### `open()`

- A função `open()` é usada para abrir um arquivo. Ela recebe dois parâmetros principais: o nome do arquivo e o modo de abertura.
    
- Modos comuns de abertura:
    - `'r'`: leitura (`read`) – padrão, abre o arquivo para leitura.
    
    - `'w'`: escrita (`write`) – cria um novo arquivo ou sobrescreve um arquivo existente.
    
    - '`a`': anexar (`append`) – adiciona conteúdo ao final do arquivo sem sobrescrever.
    
    - `'b'`: modo binário, usado em combinação com outros modos (`'rb'`, `'wb'`).

Exemplo de uso:

~~~py
arquivo = open('exemplo.txt', 'r')  # Abre o arquivo para leitura
~~~

---

### `read()`, `readline()`, e `readlines()`

- `read()`: Lê todo o conteúdo do arquivo.

- `readline()`: Lê uma linha por vez.

- `readlines()`: Lê todas as linhas e as retorna em uma lista.

Exemplo de uso:

~~~py
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
~~~

---

### `write()` e `writelines()`

- `write()`: Escreve uma string no arquivo.

- `writelines()`: Escreve uma lista de strings no arquivo.

Exemplo de uso:

~~~py
with open('exemplo.txt', 'w') as arquivo:
    arquivo.write("Olá, mundo!\n")
    arquivo.write("Outra linha.")
~~~

---

### Uso de `with`

- O uso do bloco `with` é recomendado para manipulação de arquivos, pois ele garante que o arquivo será fechado automaticamente após a execução do bloco.

~~~py
with open('exemplo.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
~~~

*Aqui, o arquivo é fechado automaticamente ao sair do bloco with, mesmo que ocorra uma exceção.*

---

# Manipulação de Arquivos CSV

- Arquivos CSV (Comma-Separated Values) são usados para armazenar dados tabulares. Python possui o módulo `csv` para facilitar a leitura e escrita desses arquivos.

### Leitura de Arquivos CSV

Exemplo:

~~~py
import csv

with open('dados.csv', 'r') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)
~~~

---

### Escrita em Arquivos CSV

~~~py
import csv

dados = [
    ['Nome', 'Idade', 'Cidade'],
    ['João', 28, 'São Paulo'],
    ['Maria', 34, 'Rio de Janeiro']
]

with open('dados.csv', 'w', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerows(dados)
~~~

---

# Manipulação de Arquivos JSON

- Arquivos JSON (JavaScript Object Notation) são usados para armazenar e transferir dados em formato de texto. Python possui o módulo `json` para facilitar a manipulação desses arquivos.

Leitura de Arquivos JSON

Exemplo:

~~~py
import json

with open('dados.json', 'r') as arquivo_json:
    dados = json.load(arquivo_json)
    print(dados)
~~~

---

### Escrita em Arquivos JSON

Exemplo:

~~~py
import json

dados = {
    'nome': 'João',
    'idade': 28,
    'cidade': 'São Paulo'
}

with open('dados.json', 'w') as arquivo_json:
    json.dump(dados, arquivo_json, indent=4)
~~~

---

## Resumo

- `open()` é usado para abrir arquivos em diferentes modos (`r`, `w`, `a`).
    
- Leitura: `read()`, `readline()`, `readlines()`.

- Escrita: `write()`, `writelines()`.
    
- Bloco `with`: Garante o fechamento automático do arquivo.
    
- **CSV** e **JSON** são formatos comuns, com módulos (`csv`, `json`) específicos para manipulação.

*Esses conceitos são fundamentais para trabalhar com leitura e escrita de arquivos em Python e são frequentemente usados em tarefas de processamento de dados.*

---