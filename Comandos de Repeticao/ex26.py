# Exercício 26: Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n. Calcule o valor do seno desse ângulo usando a respectiva série de Taylor.

# Implemente aqui a solução do exercício
def factorial(x):
    fat = 1
    for i in range(x, 0, -1):
        fat *= i
    return fat

def funcao(x, n):
    taylor = 0
    for k in range(n+1):
        termo = ((-1)**k * x**(2*k + 1)) / factorial(2*k + 1)
        taylor += termo
    return taylor