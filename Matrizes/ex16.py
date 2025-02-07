# Exercício 16
# Faça um programa que carregue uma matriz 12 × 13 e divida todos os elementos de cada linha pelo maior elemento em módulo daquela linha. Escreva a matriz original e a modificada.
#--------------------------------------------------

# Escreva a solução aqui:


matriz = []

for i in range(12):
    linha = []
    for j in range(13):
        linha.append(int(input()))
    matriz.append(linha)

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(f"{matriz[i][j]:.2f}", end=" ")
    print()

print()
modificada = matriz
for i in range(len(modificada)):

    maior = 0
    for j in range(len(modificada[i])):
        atual = abs(modificada[i][j])
        if atual > maior:
            maior = atual

    for j in range(len(modificada[i])):
        modificada[i][j] /= maior

for i in range(len(modificada)):
    for j in range(len(modificada[i])):
        print(f"{modificada[i][j]:.2f}", end=" ")
    print()