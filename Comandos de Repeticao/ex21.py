# Exercício 21: Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1.

# Implemente aqui a solução do exercício
def imprima_n_vezes(x, n):
    for _ in range(n):
        print(x, end=" ")

def funcao(n):
    for i in range(1, n + 1):
        espaços = n - i
        # print(' ' * espaços + '*' * (2 * i - 1))
        imprima_n_vezes(" ", espaços)
        imprima_n_vezes("*", (2 * i - 1))
        print()

funcao(5)