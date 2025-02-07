matriz = []

for i in range(20):
    linha = []
    for j in range(20):
        linha.append(int(input()))
    matriz.append(linha)

maior = float('-inf')
coordenadax = coordenaday = 0
direcao = ''

# Verifica na vertical e horizontal
for i in range(20):
    for j in range(17):
        # Vertical
        num = matriz[j][i] * matriz[j+1][i] * matriz[j+2][i] * matriz[j+3][i]
        if num > maior:
            maior = num
            coordenadax, coordenaday, direcao = j, i, 'baixo'
        
        # Horizontal
        num = matriz[i][j] * matriz[i][j+1] * matriz[i][j+2] * matriz[i][j+3]
        if num > maior:
            maior = num
            coordenadax, coordenaday, direcao = i, j, 'direita'

# Verifica nas diagonais
for i in range(17):
    for j in range(17):
        # Diagonal direita baixo
        num = matriz[i][j] * matriz[i+1][j+1] * matriz[i+2][j+2] * matriz[i+3][j+3]
        if num > maior:
            maior = num
            coordenadax, coordenaday, direcao = i, j, 'direita baixo'
        
        # Diagonal esquerda baixo
        num = matriz[i][j+3] * matriz[i+1][j+2] * matriz[i+2][j+1] * matriz[i+3][j]
        if num > maior:
            maior = num
            coordenadax, coordenaday, direcao = i, j+3, 'esquerda baixo'

print(maior)
print(coordenadax)
print(coordenaday)
print(direcao)