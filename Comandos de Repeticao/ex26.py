# Exercício 26: Faça uma função que receba como parâmetro o ângulo x (em radianos) e um valor inteiro positivo n. Calcule o valor do seno desse ângulo usando a respectiva série de Taylor.

# Implemente aqui a solução do exercício
import math

def funcao(x, n):
    taylor = 0
    for k in range(n):
        termo = ((-1)**k * x**(2*k + 1)) / math.factorial(2*k + 1)
        taylor += termo
    return taylor

x = float(input())
n = int(input())

# Cálculo e exibição do resultado
resultado = funcao(x, n)
print(resultado)
