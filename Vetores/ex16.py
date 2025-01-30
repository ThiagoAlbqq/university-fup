# Exercício 16
# Crie uma função que recebe um vetor e retorna um novo vetor sem elementos repetidos.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor):
    novo_vetor = []
    for i in range(len(vetor)):
        if vetor.count(vetor[i]) == 1:
            novo_vetor.append(vetor[i])
    return novo_vetor
