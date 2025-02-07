# Exercício 12
# Leia uma matriz 4 × 4. Calcule e imprima sua transposta. Não use comandos nem funções do Python ou de suas bibliotecas que já façam isso.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)

transposta = []
for i in range(len(matriz[0])):
    coluna = []
    for j in range(len(matriz)):
        coluna.append(matriz[j][i])
    transposta.append(coluna)

for i in range(len(transposta)):
    for j in range(len(transposta[i])):
        print(transposta[i][j], end=" ")
    print()