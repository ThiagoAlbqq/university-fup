# Exercício 18
# Crie uma função que recebe dois vetores A e B e retorna um vetor C com a diferença A - B.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor1, vetor2):
    vetor3 = []
    for i in range(len(vetor1)):
        vetor3.append(vetor1[i] - vetor2[i])
    return vetor3