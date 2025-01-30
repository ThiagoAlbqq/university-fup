# Exercício 8
# Leia um vetor com 15 posições e some os valores ímpares.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
impares = []
for i in range(15):
    vetor.append(int(input()))

soma = 0
for i in range(len(vetor)):
    if not vetor[i] % 2 == 0:
        impares.append(vetor[i])
        soma += vetor[i]

print(soma)

for i in range(len(impares)):
    print(impares[i])