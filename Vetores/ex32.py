# Exercício 32
# Gerencie uma lista de até 5 nomes de alunos, permitindo buscas parciais e exibindo os índices encontrados.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []

while True:
    aluno = input("Aluno: ")
    vetor.append(aluno)

    if len(vetor) == 5:    
        break

    continuar = input("Deseja inserir novo aluno? [S/N] ").strip().upper()

    if continuar == 'N':
        break 

pesquisa = input("Aluno para pesquisa: ")

for i in range(len(vetor)):
    if pesquisa in vetor[i]:
        print(vetor[i])
        print(i)
