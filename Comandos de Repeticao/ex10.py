# Exercício 10: Faça uma função que receba um inteiro x e um inteiro não-negativo n e, usando laço de repetição, calcule x^n e retorne o resultado.

# Implemente aqui a solução do exercício
def funcao(x, n):
    resultado = 1
    for _ in range(n):
        resultado *= x
    return resultado