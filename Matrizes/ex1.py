# Exercício 1
# Leia uma matriz 4 × 4 de inteiros, conte e escreva quantos valores maiores que 10 ela possui.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)

contador = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > 10:
            contador += 1

print(contador)