# Exercício 14
# Preencha um vetor com 12 números reais aleatórios no intervalo [-10, 10] e conte quantos são negativos e some os positivos.
#--------------------------------------------------

# Escreva a solução aqui:

import random

random.seed(int(input()))

vetor = []
for i in range(12):
    vetor.append(random.uniform(-10,10))

neg = 0
pos = 0
for i in range(len(vetor)):
    if vetor[i] < 0:
        neg += 1
    else: 
        pos += vetor[i]

print(neg)
print(f"{pos:.2f}")