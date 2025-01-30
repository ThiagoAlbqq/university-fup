# Exercício 11
# Leia as notas de 15 alunos, calcule e exiba a média geral.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
for i in range(15):
    vetor.append(float(input()))

soma = 0
for i in range(len(vetor)):
    soma += vetor[i]

media = soma/ len(vetor)
print(f"{media:.2f}")