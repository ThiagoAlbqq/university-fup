# Exercício 18: Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.

# Implemente aqui a solução do exercício
# Deus é muito bom, criou a coquinha para nos salvar.

import math

def funcao(p):
    fatorial = 1
    soma = 0
    for i in range(p, 0, -1):
        fatorial *= i
    print(fatorial)
    casas = int(math.log10(fatorial))
    for j in range(casas, -1, -1):
        num = fatorial // (10 ** j)
        fatorial = fatorial % (10 ** j)
        soma += num

    return soma

print(funcao(7))