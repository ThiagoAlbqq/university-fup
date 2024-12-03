# Exercício 15: Faça uma função que, dado um valor N inteiro e positivo, calcule o valor de E, conforme a fórmula a seguir: E = 1 + 1/1! + 1/2! + 1/3! ... 1/n!.

# Implemente aqui a solução do exercício
#Confie no verdadeiro
from math import factorial

def funcao(n):
    e = 1
    for i in range(1,n+1):
        e += 1/factorial(i)
    return e