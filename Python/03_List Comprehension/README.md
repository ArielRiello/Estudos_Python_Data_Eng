
# Compreensão de Listas (List Comprehension)

- List Comprehension é uma forma concisa e eficiente de criar listas em Python. Ele permite gerar uma nova lista aplicando uma expressão a cada elemento de uma sequência (como uma lista, tupla, ou string) e opcionalmente filtrando elementos com uma condição.

---

### Estrutura Básica

A estrutura básica do List Comprehension é:

~~~py
nova_lista = [expressao for elemento in sequencia]
~~~

- **expressao:** A operação ou transformação a ser aplicada a cada elemento.
- **elemento:** Cada item na sequência original.
- **sequencia:** A lista, tupla, string ou outro iterável a ser percorrido.

Exemplo Simples

~~~py
quadrados = [x ** 2 for x in range(1, 6)]
print(quadrados)  # Resultado: [1, 4, 9, 16, 25]
~~~

---

### Com Condicional (Filtro)

- Você pode adicionar uma condição ao final da expressão para filtrar elementos.

~~~py
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Resultado: [0, 2, 4, 6, 8]
~~~

---

### Usando else (Operações Condicionais)

- Você também pode usar if-else diretamente na expressão para aplicar transformações diferentes dependendo de uma condição.

~~~py
resultado = [x if x % 2 == 0 else x * 2 for x in range(10)]
print(resultado)  # Resultado: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
~~~

---

### Aninhamento de Loops (List Comprehension Aninhado)

- É possível usar loops aninhados para gerar combinações de elementos.

~~~py
combinacoes = [(x, y) for x in range(3) for y in range(3)]
print(combinacoes)

# Resultado: [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
~~~

---

### Aplicações Comuns de List Comprehension

1. **Transformação de dados:** Aplicar uma função ou operação a todos os elementos de uma lista.

2. **Filtragem de elementos:** Criar uma sublista com base em uma condição.

3. **Combinações de listas:** Criar combinações de elementos de diferentes listas.

### Vantagens

- **Sintaxe concisa:** Reduz o código, tornando-o mais legível.

- **Desempenho:** Pode ser mais rápido do que usar loops for tradicionais.

Exemplos adicionais

1. Converter todos os caracteres para maiúsculas em uma lista de strings:

~~~py
palavras = ["python", "list", "comprehension"]
maiusculas = [palavra.upper() for palavra in palavras]
print(maiusculas)  # Resultado: ['PYTHON', 'LIST', 'COMPREHENSION']
~~~

2. Obter os números ímpares ao quadrado de uma lista:

~~~py
numeros = [1, 2, 3, 4, 5]
impares_quadrados = [x ** 2 for x in numeros if x % 2 != 0]
print(impares_quadrados)  # Resultado: [1, 9, 25]
~~~

*O List Comprehension é uma ferramenta poderosa para manipulação de listas em Python, facilitando a escrita de código mais claro e eficiente.*

---