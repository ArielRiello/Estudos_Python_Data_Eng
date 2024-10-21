
# Tratamento de Exceções

- O tratamento de exceções em Python permite que você lide com erros de forma controlada, evitando que seu programa termine abruptamente quando ocorrer um erro. Os blocos `try`, `except` e `finally` são usados para capturar e tratar exceções, garantindo um fluxo mais seguro para o código.

---

### O que é uma Exceção?

- Uma exceção é um erro que ocorre durante a execução do programa, interrompendo o fluxo normal do código.

- Exceções comuns incluem erros de divisão por zero, variáveis não definidas e acesso a índices inexistentes em uma lista.

Exemplo de uma exceção:

~~~py
resultado = 10 / 0  # Gera uma exceção ZeroDivisionError
~~~

---

### Estrutura Básica do Tratamento de Exceções

A estrutura básica para tratar exceções em Python é o uso do bloco `try` e `except`:

~~~py
try:
    # Código que pode gerar uma exceção
    resultado = 10 / 0
except ZeroDivisionError:
    # Código para lidar com a exceção
    print("Erro: Divisão por zero não é permitida.")
~~~

---

### Bloco `try` e `except`


- `try`: Contém o código que pode gerar uma exceção. Se ocorrer um erro, a execução pula para o bloco`except`.

- `except`: Define o código a ser executado se uma exceção do tipo especificado ocorrer.

Exemplo:

~~~py
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
~~~

---

### Bloco `finally`

- O bloco finally é executado independentemente de uma exceção ter ocorrido ou não.

- É geralmente usado para liberar recursos externos, como fechar arquivos ou conexões de banco de dados.

Exemplo:

~~~py
try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não foi encontrado.")
finally:
    arquivo.close()  # O arquivo será fechado independentemente de ter ocorrido um erro ou não
~~~

---

### Bloco `else`

- O bloco `else` é executado apenas se nenhuma exceção ocorrer no bloco `try`.

- É usado para separar o código que só deve ser executado se o `try` for bem-sucedido.

Exemplo:

~~~py
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: Você deve digitar um número inteiro.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
else:
    print(f"O resultado é {resultado}.")
finally:
    print("Execução finalizada.")
~~~

---

### Tratando Exceções Genéricas

- Se não for especificado o tipo de exceção, o bloco `except` captura qualquer erro.

Exemplo:

~~~py
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except Exception as e:
    print(f"Ocorreu um erro: {e}")
~~~

---

### Levantando Exceções com `raise`

- O comando `raise` é usado para gerar uma exceção manualmente.

- Pode ser útil para validar condições específicas no código.

Exemplo:

~~~py
def verificar_idade(idade):
    if idade < 18:
        raise ValueError("Idade deve ser maior ou igual a 18.")
    print("Idade válida.")

try:
    verificar_idade(15)
except ValueError as e:
    print(f"Erro: {e}")
~~~

---

### RESUMO

- `try`: Envolve o código que pode gerar uma exceção.

- `except`: Captura a exceção e permite tratar o erro.

- `finally`: Código que será executado sempre, independentemente de uma 
exceção ocorrer.

- `else`: Executa se o código no bloco `try` for bem-sucedido.

- `raise`: Permite gerar uma exceção manualmente.

*O tratamento de exceções é essencial para tornar os programas mais robustos e seguros, garantindo que erros inesperados sejam tratados de forma controlada.*

---