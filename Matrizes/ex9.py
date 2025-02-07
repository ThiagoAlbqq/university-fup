# Exercício 9
# Leia uma matriz 4 × 4. Calcule a soma dos elementos que estão abaixo da diagonal principal. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)

soma = 0
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if j < i:
            soma += matriz[i][j]

print(soma)