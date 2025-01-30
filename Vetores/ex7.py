# Exercício 7
# Leia um vetor com 15 posições e conte quantos valores são pares.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
pares = []
for i in range(15):
    vetor.append(int(input()))

for number in vetor:
    if number % 2 == 0:
        pares.append(number)

print(len(pares))

for number in pares:
    print(number)