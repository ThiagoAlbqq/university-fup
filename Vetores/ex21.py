# Exercício 21
# Preencha um vetor de tamanho 70 usando a fórmula (i + 5*i) % (i + 1) e exiba-o.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = []
for i in range(70):
    num = (i + 5*i) % (i + 1)
    vetor.append(num)

print(vetor)