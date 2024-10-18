
# Manipulação de Listas, Dicionários e Conjuntos

### Listas

- Listas são coleções ordenadas de elementos, que podem ser de qualquer tipo (números, strings, etc.). Os itens são mutáveis, ou seja, podem ser alterados após a criação.

Como criar uma lista:

~~~py
numeros = [1, 2, 3, 4, 5]
frutas = ["maçã", "banana", "laranja"]
~~~

Principais operações com listas:

Acessar elementos:

~~~py
print(numeros[0])  # Resultado: 1
print(frutas[-1])  # Resultado: "laranja" (último elemento)
~~~

Adicionar elementos:

~~~py
frutas.append("uva")  # Adiciona "uva" ao final da lista
frutas.insert(1, "manga")  # Insere "manga" na posição 1
~~~

Remover elementos:

~~~py
frutas.remove("banana")  # Remove "banana" da lista
fruta_removida = frutas.pop(0)  # Remove o primeiro elemento e retorna o valor removido
~~~

Fatiamento (slicing):

~~~py
sublista = numeros[1:4]  # Pega os elementos do índice 1 até 3
~~~

Iterar sobre uma lista:

~~~py
for fruta in frutas:
    print(fruta)
~~~

---

### Dicionários

- Dicionários são coleções de pares de chave-valor. Eles são mutáveis e os elementos são acessados por chave, não por índice.

Como criar um dicionário:

~~~py
aluno = {"nome": "João", "idade": 25, "curso": "Engenharia"}
~~~

Principais operações com dicionários:

Acessar valores:

~~~py
print(aluno["nome"])  # Resultado: "João"
~~~

Adicionar ou atualizar valores:

~~~py
aluno["nota"] = 8.5  # Adiciona uma nova chave "nota"
aluno["idade"] = 26  # Atualiza o valor da chave "idade"
~~~

Remover elementos:

~~~py
del aluno["curso"]  # Remove a chave "curso"
nota_removida = aluno.pop("nota", None)  # Remove "nota" e retorna o valor, ou None se não existir
~~~

Iterar sobre dicionários:

~~~py
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")
~~~

---

### Conjuntos (Sets)

- Conjuntos são coleções não ordenadas de elementos únicos. Não permitem elementos duplicados e são usados para operações de conjunto como união, interseção e diferença.

Como criar um conjunto:

~~~py
conjunto_numeros = {1, 2, 3, 4, 5}
conjunto_vazio = set()  # Criação de um conjunto vazio
~~~

Principais operações com conjuntos:

Adicionar e remover elementos:

~~~py
conjunto_numeros.add(6)  # Adiciona 6 ao conjunto
conjunto_numeros.remove(3)  # Remove 3 do conjunto
~~~

Operações de conjuntos:

~~~py
conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União
uniao = conjunto_a | conjunto_b  # Resultado: {1, 2, 3, 4, 5}

# Interseção
intersecao = conjunto_a & conjunto_b  # Resultado: {3}

# Diferença
diferenca = conjunto_a - conjunto_b  # Resultado: {1, 2}
~~~

---

### Diferenças Principais entre Listas, Dicionários e Conjuntos

- **Listas:** Ordenadas, mutáveis, permitem elementos duplicados.

- **Dicionários:** Coleções de pares chave-valor, mutáveis, acessíveis por chave.

- **Conjuntos:** Não ordenados, elementos únicos, não permitem duplicados, ideais para operações de conjunto.

---