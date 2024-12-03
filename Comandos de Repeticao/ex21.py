# Exercício 21: Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1.

# Implemente aqui a solução do exercício
def funcao(n):
    for i in range(1, n + 1):
        espaços = n - i
        print(' ' * espaços + '*' * (2 * i - 1))

