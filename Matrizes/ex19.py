# Exercício 19
# Faça um programa que gere uma matriz m × n de inteiros aleatórios. Mostre a matriz e calcule e mostre a média dos elementos das linhas pares da matriz e a quantidade de números negativos e divisíveis por 3 das linhas ímpares da matriz. A quantidade de linhas m, a quantidade de colunas n, a semente dos números aleatórios e o intervalo de geração serão dados como entrada para o programa.
#--------------------------------------------------

# Escreva a solução aqui:

import random

m = int(input())
n = int(input())
random.seed(int(input()))
inicio = int(input())
final = int(input())

matriz = []

for i in range(m):
    linha = []
    for j in range(n):
        linha.append(random.randint(inicio, final))
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]}", end=" ")
    print()


for i in range(len(matriz)):
    negativos_divisores_de_tres = 0
    media = 0
    for j in range(len(matriz[i])):
        if i % 2 == 0:
            media += matriz[i][j]/len(matriz[i])
        else:
            if (matriz[i][j] < 0) and (matriz[i][j] % 3) == 0:
                negativos_divisores_de_tres += 1
    if i % 2 == 0:
        print(f"{media:.2f}")
    else:
        print(negativos_divisores_de_tres)
        
