"""
Desafio 2: Classificação de Alunos

    - Crie um programa que peça ao usuário o nome e as notas (de 0 a 10) de 5 alunos.
    
    - Armazene essas informações usando variáveis e listas.
    
    - Calcule a média das notas para cada aluno.
    
    - Use estruturas condicionais para classificar os alunos de acordo com a média: "Aprovado" (média >= 7), "Recuperação" (5 <= média < 7), ou "Reprovado" (média < 5).
    
    - Use um loop for para exibir o nome, as notas e a situação de cada aluno.
    
"""

class AlunosNotas:
    def __init__(self):
        self.alunos_notas = []

    def adicionar_aluno_nota(self, nome, nota):
        novo_aluno_nota = {nome: nota}
        self.alunos_notas.append(novo_aluno_nota)

    def calcular_media_aluno(self):
        for aluno in self.alunos_notas:
            for nome, notas in aluno.items():
                media = sum(notas) / len(notas)
                print(f"A média do aluno {nome} é {media:.2}")

colecao = AlunosNotas()

while True:
    try:
        
        nome = input("\nInforme o nome do aluno: ")
        qtd_notas = int(input("\nInforme a quantidade de notas para tirar a média: "))

        notas_aluno = []

        for i in range(qtd_notas):
            nota = int(input(f"Informe a nota {i+1}: "))
            notas_aluno.append(nota)

        colecao.adicionar_aluno_nota(nome, notas_aluno)

        continuar_sair = ""

        while continuar_sair not in ["SIM", "NAO"]:
            continuar_sair = input("""\nDeseja adicionar um novo aluno ao calculo de médias?\nDigite:\n"SIM" para continuar adicionando\n"NAO" para realizar os calculos\n""").upper()
            
        if continuar_sair == "SIM":
            continue
        if continuar_sair == "NAO":
            colecao.calcular_media_aluno()
            break

    except ValueError:
        print("Erro: Por favor, insira um número válido para a quantidade de notas ou para a nota.")