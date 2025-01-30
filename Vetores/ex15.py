# Exercício 15
# Leia um vetor de 10 posições e verifique se há valores repetidos, exibindo-os.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
for i in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    for j in range(i + 1, len(vetor)):
        if vetor[i] == vetor[j]:
            print(vetor[i])