# Exercício 20: Escreva uma função que gera um triângulo lateral de altura 2 × n − 1 e n de largura.

# Implemente aqui a solução do exercício
# Pipipipipriguicaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
def funcao(n):
    for i in range(1, n + 1):
        print("*" * i)
    for i in range(n - 1, 0, -1):
        print("*" * i)
