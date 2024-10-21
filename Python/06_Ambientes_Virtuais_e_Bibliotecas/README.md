
# Ambientes Virtuais e Bibliotecas em Python

  O uso de ambientes virtuais e bibliotecas é uma prática comum em Python para garantir que os projetos tenham suas próprias dependências isoladas e não conflitem com outras aplicações ou bibliotecas instaladas no sistema.
  
---

### O que são Ambientes Virtuais?

Um ambiente virtual é um diretório específico no sistema onde são instaladas as bibliotecas e dependências de um projeto Python. Isso permite que cada projeto tenha suas próprias versões de bibliotecas, evitando conflitos entre diferentes projetos.

Por que usar ambientes virtuais?

- Isolamento: Cada projeto pode ter suas próprias dependências, sem interferir em outros projetos.

- Facilidade de gerenciamento: É possível instalar bibliotecas 
    específicas para cada projeto sem afetar a instalação global de Python.

- Reprodutibilidade: Permite que outras pessoas ou sistemas reproduzam o ambiente exato do projeto, usando um arquivo de dependências 
    (`requirements.txt`).

---

### Como Criar e Usar Ambientes Virtuais

Ferramenta venv

O módulo `venv` faz parte da biblioteca padrão do Python e é usado para criar ambientes virtuais.
Passos para criar e ativar um ambiente virtual:

1. Criar um ambiente virtual:

~~~bash
python3 -m venv nome_do_ambiente
~~~

*Isso criará uma pasta chamada `nome_do_ambiente` com o ambiente virtual.*

2. Ativar o ambiente virtual

~~~bash
# No Windows:
nome_do_ambiente\Scripts\activate

# No Linux ou macOS:
source nome_do_ambiente/bin/activate
~~~

3. Desativar o ambiente virtual

~~~bash
deactivate
~~~

*Quando o ambiente virtual está ativo, todas as bibliotecas instaladas serão específicas para aquele ambiente.*

---

### Alternativas para Gerenciamento de Ambientes Virtuais

Além de `venv`, existem outras ferramentas para gerenciar ambientes virtuais:

### `virtualenv`

- Funciona de maneira similar ao `venv`, mas é uma ferramenta externa que pode ser mais eficiente em alguns casos.

- Para instalar o `virtualenv`:
    ~~~bash
    pip install virtualenv
    ~~~

### `conda`

- Um gerenciador de ambientes e pacotes utilizado principalmente em ciência de dados.

- Funciona com pacotes que não são exclusivos do Python (como bibliotecas C).

---

### Gerenciamento de Bibliotecas com `pip`

O `pip` é o gerenciador de pacotes padrão do Python, usado para instalar, atualizar e remover bibliotecas.

Comandos básicos do `pip`:

- Instalar uma biblioteca
    ~~~bash
    pip install nome_da_biblioteca
    ~~~

- Instalar uma biblioteca com versão específica
    ~~~bash
    pip install nome_da_biblioteca==versao
    ~~~

- Listar bibliotecas instaladas
    ~~~bash
    pip list
    ~~~

- Atualizar uma biblioteca
    ~~~bash
    pip install --upgrade nome_da_biblioteca
    ~~~

- Desinstalar uma biblioteca
    ~~~bash
    pip uninstall nome_da_biblioteca
    ~~~

---

### Boas Práticas para Uso de Ambientes Virtuais e Bibliotecas

- Sempre usar um ambiente virtual: Nunca instale bibliotecas diretamente no Python do sistema, para evitar conflitos e problemas de versão.

- Manter o arquivo `requirements.txt` atualizado: Gere o `requirements.txt` sempre que adicionar uma nova biblioteca ao projeto.

- Escolher versões específicas para bibliotecas: Isso ajuda a garantir que o projeto funcione de maneira previsível em diferentes ambientes.

---

### RESUMO

- Ambientes Virtuais: Permitem isolar as dependências dos projetos.

- `venv`: Ferramenta padrão para criar ambientes virtuais.

- `pip`: Gerenciador de pacotes para instalar, atualizar e remover bibliotecas.

- `requirements.txt`: Arquivo para listar as dependências do projeto e facilitar a reprodução do ambiente.

*O uso de ambientes virtuais e bibliotecas é uma prática fundamental para o desenvolvimento Python, garantindo que os projetos sejam facilmente gerenciáveis e livres de conflitos de dependências.*

---