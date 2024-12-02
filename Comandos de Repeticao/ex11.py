# Exercício 11: Faça uma função que receba um valor inteiro n ≥ 0 e calcule o seu fatorial n!. Lembrete: 0! = 1.

# Implemente aqui a solução do exercício
def funcao(x):
    fat = 1
    for i in range(x, 0, -1):
        fat *= i
    return fat
x = int(input())
print(funcao(x))