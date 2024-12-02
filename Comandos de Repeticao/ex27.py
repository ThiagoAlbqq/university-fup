# Exercício 27: Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número.

# Implemente aqui a solução do exercício
def funcao(n):
    fatEx = n
    for i in range(n-1, 0, -1):
        fatEx **= i
    return fatEx
print(funcao(3))
