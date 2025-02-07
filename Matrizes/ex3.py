# Exercício 3
# Faça um programa que preenche uma matriz de tamanho nxn com o produto do valor da linha e da coluna de cada elemento. Em seguida, imprima na tela a matriz, em forma de tabela.
#--------------------------------------------------

# Escreva a solução aqui:

n = int(input())
matriz = []

for i in range(n):
    linha = []
    for j in range(n):
        linha.append(j*i)
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()