# Exercício 26
# Crie uma função que recebe dois vetores e retorna um vetor com a diferença (elementos do primeiro que não estão no segundo).
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor1, vetor2):
    novo_vetor = []
    for i in range(len(vetor1)):
        if not(vetor1[i] in vetor2) and not(vetor1[i] in novo_vetor):
            novo_vetor.append(vetor1[i])
    return novo_vetor
