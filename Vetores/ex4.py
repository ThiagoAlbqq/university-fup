# Exercício 4
# Leia 10 valores inteiros e exiba-os na ordem inversa.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []

for i in range(10):
    vetor.append(int(input()))


vetor.reverse()
for number in vetor:
    print(number)