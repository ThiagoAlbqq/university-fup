# Exercício 13
# Crie uma função que recebe um vetor de notas e retorna a média, o desvio padrão e a quantidade de notas menores que 7.0.
#--------------------------------------------------

# Escreva a solução aqui:

def funcao(notas):
    soma = 0
    contador = 0
    for i in range(len(notas)):
        soma += notas[i]
        if notas[i] < 7:
            contador += 1

    media = soma / len(notas)

    soma_quadrados_diferencas = 0
    for i in range(len(notas)):
        diferenca = notas[i] - media
        soma_quadrados_diferencas += diferenca**2

    desvio_padrao = (soma_quadrados_diferencas / len(notas))**0.5

    return media, desvio_padrao, contador