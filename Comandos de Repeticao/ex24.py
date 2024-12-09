# Exercício 24: O Triângulo de Pascal é um triângulo numérico infinito formado por números binomiais Cn,k, onde n representa o número da linha (posição horizontal) e k representa o número da coluna (posição vertical), iniciando a contagem a partir do zero.

# Implemente aqui a solução do exercício
def factorial(x):
    fat = 1
    for i in range(x, 0, -1):
        fat *= i
    return fat

def funcao(n):
    linha = 0
    for linha in range(n):
        for coluna in range(linha + 1):
            valor = factorial(linha) // (factorial(coluna) * factorial(linha - coluna))
            print(valor, end=" ")
        print()

n = int(input())
funcao(n)

