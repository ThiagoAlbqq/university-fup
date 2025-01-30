# Exercício 17
# Crie uma função que recebe um vetor e um número X e retorna os múltiplos de X no vetor.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor, num):
    aux = []
    for i in range(len(vetor)):
        if vetor[i] % num == 0:
            aux.append(vetor[i])
    return aux