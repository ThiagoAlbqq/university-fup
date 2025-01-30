# Exercício 6
# Leia um vetor de 8 posições e dois índices X e Y, exibindo a soma dos valores dessas posições.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
for i in range(8):
    vetor.append(float(input()))

x = int(input())
y = int(input())

soma = vetor[x] + vetor[y]

print(f"{soma:.2f}")