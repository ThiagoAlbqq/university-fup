# Exercício 24
# Crie uma função que recebe dois vetores e retorna um vetor com a interseção sem elementos repetidos.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor1, vetor2):
    novo_vetor = []
    for i in range(len(vetor1)):
        if (vetor1[i] in vetor2) and not(vetor1[i] in novo_vetor):
            novo_vetor.append(vetor1[i])
    return novo_vetor
