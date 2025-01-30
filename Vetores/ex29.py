# Exercício 29
# Crie uma função que ordena um vetor do maior para o menor sem usar funções de ordenação do Python.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor):
    for i in range(len(vetor)):
        for j in range(len(vetor) - i - 1):
            if vetor[j] < vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]
    return vetor

