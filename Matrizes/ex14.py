# Exercício 14
# Faça um programa que leia duas matrizes A e B de tamanho 4 × 5 cada uma. Calcule a matriz C = A + B. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.
#--------------------------------------------------

# Escreva a solução aqui:

matriz1 = []
matriz2 = []

for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz1.append(linha)


for i in range(4):
    linha = []
    for j in range(5):
        linha.append(int(input()))
    matriz2.append(linha)

somada = []
for i in range(len(matriz1)):
    linha = []
    for j in range(len(matriz1[i])):
        linha.append(matriz1[i][j] + matriz2[i][j])
    somada.append(linha)

for i in range(len(somada)):
    for j in range(len(somada[i])):
        print(somada[i][j], end=" ")
    print()