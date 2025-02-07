# Exercício 7
# Gerar e imprimir uma matriz A de tamanho 10 × 10, onde seus elementos são da forma: A[i][j] = 2 * i + 7 * j - 2, se i < j; A[i][j] = 3 * i ** 2 - 1, se i = j; A[i][j] = 4 * i ** 3 - 5 * j ** 2 + 1, se i > j.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(10):
    linha = []
    for j in range(10):
        if i < j:
            linha.append(2 * i + 7 * j - 2)
        elif i == j:
            linha.append(3 * i ** 2 - 1)
        elif i > j:
            linha.append(4 * i ** 3 - 5 * j ** 2 + 1)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()