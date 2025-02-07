# Exercício 18
# Gere uma matriz 5 × 5 com inteiros aleatórios no intervalo [1, 20], encontrados a partir de uma semente dada como entrada. Escreva um programa que transforme a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os elementos acima da diagonal principal. Imprima a matriz original e a matriz transformada. Não use nenhum comando de decisão (se/então/senão).
#--------------------------------------------------

# Escreva a solução aqui:
import random

random.seed(int(input()))

matriz = []
modificada = []
for i in range(5):
    linha = []
    for j in range(5):
        linha.append(int(random.randint(1, 20)))
    matriz.append(linha)

for i in range(len(matriz)):
    linha = []
    for j in range(len(matriz[i])):
        linha.append(matriz[i][j])
    modificada.append(linha)


for i in range(len(modificada)):
    for j in range(i + 1, len(modificada[i])):
        modificada[i][j] = 0

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:3}", end=" ")
    print()

print()

for i in range(len(modificada)):
    for j in range(len(modificada[i])):
        print(f"{modificada[i][j]:3}", end=" ")
    print()