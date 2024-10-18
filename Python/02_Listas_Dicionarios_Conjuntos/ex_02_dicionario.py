""""
Exercício com Dicionário

Crie um dicionário para armazenar as notas de três matérias de um aluno. As chaves devem ser os nomes das matérias e os valores, as notas.

    - Calcule a média das notas e exiba o resultado.
    - Atualize a nota de uma das matérias.
    - Adicione uma nova matéria e sua respectiva nota ao dicionário.
    - Exiba o dicionário atualizado.

"""

def aluno_notas(nome, nota_mat, nota_fis, nota_qui):
    aluno = {
        "Nome": nome,
        "Matematica": nota_mat,
        "Fisica": nota_fis,
        "Quimica": nota_qui,
    }
    print(aluno)


nome = input("Digite o nome do aluno: ")
mat = int(input("Digite a nota em Matematica: "))
fis = int(input("Digite a nota em Fisica: "))
qui = int(input("Digite a nota em Quimica: "))


aluno_notas(nome, mat, fis, qui)

# -------------------------------------------------------- #


# def aluno_notas_01(nome, nota_mat, nota_fis, nota_qui):
#     aluno = {}
#     aluno["Nome"] = nome
#     aluno["Matematica"] = nota_mat
#     aluno["Fisica"] = nota_fis
#     aluno["Quimica"] = nota_qui

#     print(aluno)

# nome = input("Digite o nome do aluno: ")
# mat = int(input("Digite a nota em Matematica: "))
# fis = int(input("Digite a nota em Fisica: "))
# qui = int(input("Digite a nota em Quimica: "))

# aluno_notas_01(nome, mat, fis, qui)

# -------------------------------------------------------- #