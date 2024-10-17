
## Fundamentos da Sintaxe e Estrutura de Código 

### 1. Variáveis e Tipos de Dados

Variáveis: São usadas para armazenar dados. Em Python, não é necessário declarar o tipo da variável, ele é inferido automaticamente.

~~~Py
nome = "Ariel Riello"   # String
idade = 32              # int
altura = float          # float
trabalhando = True      # bool
~~~

---

### 2. Operadores Básicos

**Aritméticos:** Para realizar operações matemáticas.

~~~Py
soma = 10 + 5           # adição
subtracao = 10 - 5      # subtração
multiplicacao = 10 * 5  # multiplicação
divisao = 10 / 5        # divisão (resultado float)
modulo = 10 % 3         # resto da divisão
exponenciacao = 2 ** 3  # potência
~~~

**Comparação:** Para comparar valores.

~~~Py
10 > 5      # True
10 == 10    # True
10 != 5     # True
~~~

**Lógicos:** Para realizar operações lógicas (and, or, not).

~~~Py
True and False  # False
True or False   # True
not True        # False
~~~

---

### 3. Estruturas Condicionais

Usamos if, elif (else if) e else para tomar decisões com base em condições.

~~~PY
idade = 20

if idade >= 18:
    print("É maior de idade")
elif idade == 17:
    print("Tem 17 anos")
else:
    print("É menor de idade")
~~~

### 4. Loops

**For:** Itera sobre uma sequência (lista, tupla, string).

~~~Py
# range(5) gera 0, 1, 2, 3, 4

for i in range(5):
    print(i)
~~~

**While:** Continua repetindo enquanto uma condição for verdadeira.

~~~Py
contado = 0
while contador < 5:
    print(contador)
    contador += 1
~~~

