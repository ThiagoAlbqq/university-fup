# Exercício 13
# Faça um programa que permita ao usuário entrar com uma matriz de 5 × 5 números reais. Em seguida, gere um vetor unidimensional contendo a soma dos números de cada coluna da matriz e mostre na tela esse vetor.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz.append(linha)

transposta = []
for i in range(len(matriz[0])):
    soma = 0
    for j in range(len(matriz)):
        soma += matriz[j][i]
    transposta.append(soma)

print(transposta)