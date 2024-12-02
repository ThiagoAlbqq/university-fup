# Exercício 25: Faça uma função que receba um inteiro n como parâmetro, calcule e retorne o resultado da seguinte série: S = 2/4 + 5/5 + 10/6 + ... + (n2 + 1)/(n + 3)

# Implemente aqui a solução do exercício
def funcao(n):
    s = 0
    for i in range(1, n+1):
        s += (i**2 + 1)/(i + 3)
    return s

print(funcao(2))