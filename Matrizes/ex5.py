# Exercício 5
# Leia uma matriz 5 × 5. Leia também um valor X. O programa deverá fazer uma busca desse valor na matriz e, ao final, escrever a localização (linha e coluna) ou uma mensagem de 'Não encontrado'.
#--------------------------------------------------

# Escreva a solução aqui:

matriz = []

for i in range(5):
    linha = []
    for j in range(5):
        valor = int(input())
        linha.append(valor)
    matriz.append(linha)

n = int(input())
encontrado = False
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == n:
            encontrado = True
            print(i)
            print(j)
            break 
    if encontrado:
        break


if not encontrado:
    print("Nao encontrado")