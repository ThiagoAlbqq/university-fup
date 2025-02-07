# Exercício 30
# Crie uma função que identifica segmentos iguais máximos em um vetor e retorna suas posições e tamanho.
#--------------------------------------------------

# Escreva a solução aqui:

def encontrar_segmentos_iguais_maximos(vetor):
    n = len(vetor)
    max_tamanho = 0
    posicoes = []

    for k in range(n, 1, -1):
        for i in range(n - k + 1):
            segmento = vetor[i:i + k]
            for j in range(i + 1, n - k + 1):
                if vetor[j:j + k] == segmento:
                    posicoes = [i, j]
                    max_tamanho = k
                    return posicoes[1], posicoes[2], max_tamanho
    return -1, -1, -1


vetor = [7, 9, 5, 4, 3, 8, 5, 4, 3, 6, 5, 4, 3]
vetor = [0,0,0,0,0,0,0,0,0,0]
posicoes, tamanho = encontrar_segmentos_iguais_maximos(vetor)

if tamanho >= 2:
    print(f"Segmento máximo encontrado de tamanho {tamanho} nas posições {posicoes}")
else:
    print("Não foram encontrados segmentos iguais de tamanho >= 2")