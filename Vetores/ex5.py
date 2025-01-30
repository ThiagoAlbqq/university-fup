# Exercício 5
# Armazene 10 números reais em um vetor e crie outro vetor com seus quadrados.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
quadrado = []

for i in range(10):
    vetor.append(float(input()))

for i in range(len(vetor)):
    print(f"{vetor[i]:.2f}")
    quadrado.append(vetor[i] ** 2)

for number in quadrado:
    print(f"{number:.2f}")