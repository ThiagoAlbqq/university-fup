# Exercício 6
# Leia duas matrizes 4 × 4 e escreva uma terceira matriz com os maiores valores de cada posição das matrizes lidas.
#--------------------------------------------------

# Escreva a solução aqui:

matriz1 = []
matriz2 = []

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input())
        linha.append(valor)
    matriz1.append(linha)

for i in range(4):
    linha = []
    for j in range(4):
        valor = int(input())
        linha.append(valor)
    matriz2.append(linha)

matriz3 = matriz1

for i in range(len(matriz2)):
    for j in range(len(matriz2[i])):
        if matriz3[i][j] < matriz2[i][j]:
            matriz3[i][j] = matriz2[i][j]
        print(matriz3[i][j], end=" ")
    print()