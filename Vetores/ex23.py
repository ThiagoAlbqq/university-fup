# Exercício 23
# Leia 10 inteiros e exiba apenas os números primos e suas posições no vetor.
#--------------------------------------------------

# Escreva a solução aqui:
import math
vetor = []

def eh_primo(n):
    if n < 0:
        n *= (-1)
        
    if n == 0 or n == 1:
        return False


    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True

for i in range(10):
    vetor.append(int(input()))

for i in range(len(vetor)):
    if eh_primo(vetor[i]):
        print(vetor[i])
        print(i)