# Exercício 2
# Crie um vetor A com 6 números inteiros e realize operações como soma, modificação e exibição.
#--------------------------------------------------

# Escreva a solução aqui:

vetor = [1,0,5,-2,-5,7]
soma = vetor[0] + vetor[1] + vetor[5]
print(soma)
vetor.pop(3)
vetor.insert(3, -89)
for number in vetor:
    print(number)