# Exercício 15
# Faça um programa que leia duas matrizes A e B de tamanho 5 × 5 cada uma. Calcule a matriz C = A * B. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.
#--------------------------------------------------

# Escreva a solução aqui:

matriz1 = []
matriz2 = []

for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz1.append(linha)


for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz2.append(linha)

multiplicada = []
for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz2[0])):
        linha.append(0)
    multiplicada.append(linha)

for i in range(len(matriz1)):
    for j in range(len(matriz2[0])):
        for k in range(len(matriz2)):
            multiplicada[i][j] += matriz1[i][k] * matriz2[k][j]

for i in range(len(multiplicada)):
    for j in range(len(multiplicada[i])):
        print(multiplicada[i][j], end=" ")
    print()