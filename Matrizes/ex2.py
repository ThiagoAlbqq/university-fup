# Exercício 2
# Leia um número n e crie uma matriz n×n. Preencha com 1 a diagonal principal e com 0 os demais elementos. Escreva ao final a matriz obtida, em forma de tabela. Use comandos de repetição.
#--------------------------------------------------

# Escreva a solução aqui:

n = int(input())
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        if j == i:
            linha.append(1)
        else:
            linha.append(0)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()