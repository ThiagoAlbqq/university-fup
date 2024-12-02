# Exercício 24: O Triângulo de Pascal é um triângulo numérico infinito formado por números binomiais Cn,k, onde n representa o número da linha (posição horizontal) e k representa o número da coluna (posição vertical), iniciando a contagem a partir do zero.

# Implemente aqui a solução do exercício
from math import factorial

def triangulo_de_pascal(n):
    linha = 0
    while linha < n:
        coluna = 0
        while coluna <= linha:
            valor = factorial(linha) // (factorial(coluna) * factorial(linha - coluna))
            print(valor, end=" ")
            coluna += 1
        print()
        linha += 1

n = int(input())

