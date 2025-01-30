# Exercício 9
# Leia um vetor com 10 inteiros e exiba o maior e o menor valor.
#--------------------------------------------------

# Escreva a solução aqui:


vetor = []
for i in range(10):
    vetor.append(int(input()))

maior = 0
menor = 0
for i in range(len(vetor)):
    if i == 0:
        maior = vetor[i]
        menor = vetor[i]
        continue
    if maior < vetor[i]:
        maior = vetor[i]
    if menor > vetor[i]:
        menor = vetor[i]

print(maior)
print(menor)
    