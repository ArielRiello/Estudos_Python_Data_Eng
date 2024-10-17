
# Funções em Python

### O que são Funções?

- Uma função é um bloco de código que realiza uma tarefa específica.
- Permite dividir o programa em partes menores e modulares.
- Pode receber parâmetros (entradas) e retornar valores (saídas).

---

### Como definir uma função em Python?

- Usamos a palavra-chave **def** para definir uma função, seguida pelo nome da função e parênteses.
- Dentro dos parênteses, podemos especificar os parâmetros (opcionais).
- O corpo da função é indentado e contém as instruções que ela executa.

Exemplo simples:

~~~Py
def saudacao():
    print("Olá, bem-vindo!")
~~~

Para chamar a função:

~~~Py
saudacao()  # Resultado: Olá, bem-vindo!
~~~

---

### Parâmetros e Argumentos

- Parâmetros são variáveis que aparecem na definição da função.
- Argumentos são os valores que passamos para os parâmetros ao chamar a função.

Exemplo com parâmetros:

~~~Py
def saudacao(nome):
    print(f"Olá, {nome}!")
~~~

Chamada da função:

~~~Py
saudacao("Ariel")  # Resultado: Olá, Ariel!
~~~

---

### Retorno de Valores com **return**

- O **return** finaliza a execução da função e "retorna" um valor.
- Podemos usar o valor retornado em outras partes do código.

Exemplo:

~~~Py
def somar(a, b):
    return a + b
~~~

Chamada da função e uso do retorno:

~~~Py
resultado = somar(5, 3)
print(resultado)  # Resultado: 8
~~~

---

### Funções com Parâmetros Padrão

- Podemos definir valores padrão para os parâmetros, tornando-os opcionais na chamada.

Exemplo:

~~~Py
def saudacao(nome="Visitante"):
    print(f"Olá, {nome}!")
~~~

Chamada sem argumento:

~~~Py
saudacao()  # Resultado: Olá, Visitante!
~~~

Chamada com argumento:

~~~Py
saudacao("Ariel")  # Resultado: Olá, Ariel!
~~~

---

### Funções com Vários Parâmetros

- Uma função pode ter múltiplos parâmetros separados por vírgulas.

Exemplo:

~~~Py
def calcular_area(base, altura):
    return base * altura / 2
~~~

Chamada:

~~~Py
area = calcular_area(5, 10)
print(area)  # Resultado: 25.0
~~~

---

### Funções Anônimas (Lambda)

- Funções lambda são funções anônimas e curtas.
- Usam a sintaxe **lambda parâmetros: expressão**.

Exemplo:

~~~Py
dobrar = lambda x: x * 2
print(dobrar(5))  # Resultado: 10
~~~

---