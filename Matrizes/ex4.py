# Exercício 4
# Leia uma matriz 4 × 4, imprima a matriz, imprima a localização (linha e coluna) do maior valor e imprima o maior valor.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(4):
    linha = []
    for j in range(4):
        linha.append(int(input()))
    matriz.append(linha)

maior_valor = matriz[0][0]
indice_maior_valor = [0, 0]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] > maior_valor:
            maior_valor = matriz[i][j]
            indice_maior_valor = [i, j]
        print(matriz[i][j], end=" ")
    print()

print(indice_maior_valor[0])
print(indice_maior_valor[1])
print(maior_valor)