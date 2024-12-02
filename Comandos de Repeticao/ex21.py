# Exercício 21: Escreva uma função que gera um triângulo de altura n e lados 2 × n − 1.

# Implemente aqui a solução do exercício
def funcao(n):
    temp = 1 
    for i in range(1, n):
        print("*" * temp)
        temp += 2
funcao(6)

