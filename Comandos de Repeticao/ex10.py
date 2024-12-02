# Exercício 10: Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule x^n e retorne o resultado.

# Implemente aqui a solução do exercício
x = int(input())
n = int(input())
def funcao(x, n):
    for i in range(0,n-1):
        x*=x
    return x
print(funcao(x,n))