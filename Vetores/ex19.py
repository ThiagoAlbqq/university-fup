# Exercício 19
# Crie uma função que recebe dois vetores e retorna um vetor intercalando os valores.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(vetor1, vetor2):
    vetor3 = vetor1
    for i in range(len(vetor2)):
        vetor3.insert(2*i + 1, vetor2[i])
    return vetor3