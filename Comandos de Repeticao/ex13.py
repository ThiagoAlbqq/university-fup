# Exercício 13: O número de Fibonacci Fn para n > 0 é definido da seguinte maneira:
# ◦ F1 = 1
# ◦ F2 = 1
# ◦ Fn = Fn−1 + Fn−2 para n> 2
# Faça uma função que receba um valor inteiro n e calcule Fn.

# Implemente aqui a solução do exercício
def funcao(n):
    f1 = 1
    f2 = 1
    temp = 0
    for i in range(n-2):
        temp = f1 + f2
        f1 = f2
        f2 = temp
    return temp

print(funcao(5))

