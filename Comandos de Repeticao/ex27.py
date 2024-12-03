# Exercício 27: Faça uma função não-recursiva que receba um número inteiro positivo n e retorne o fatorial exponencial desse número.

# Implemente aqui a solução do exercício
def funcao(n):
    fatEx = n
    expoente = n-1
    for i in range(1,n-1):
        expoente **= i
    return fatEx ** expoente
