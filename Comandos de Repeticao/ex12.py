# Exercício 12: Escreva uma função que receba n e k tais que k ≥ 0 e n ≥ k e calcule o coeficiente binomial Cn,k = n!/(k!*(n-k)!)

# Implemente aqui a solução do exercício
# Não testei - preguiça
from math import factorial

def funcao(n, k):
    cb = factorial(n)/(factorial(k) * factorial(n-k))
    return cb

n = int(input())
k = int(input())
print(funcao(n,k))