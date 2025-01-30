# Exercício 25
# Crie uma função que recebe dois vetores e retorna um vetor com a união sem elementos repetidos.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor1, vetor2):
    novo_vetor = []
    for i in range(len(vetor1)):
        if not(vetor1[i] in novo_vetor):
            novo_vetor.append(vetor1[i])
    for i in range(len(vetor2)):
        if not(vetor2[i] in vetor1) and (vetor2[i] not in novo_vetor):
            novo_vetor.append(vetor2[i])
    return novo_vetor
