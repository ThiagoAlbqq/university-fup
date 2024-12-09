# Exercício 18: Faça uma função que receba um número inteiro positivo P e retorne a soma dos algarismos de P! . Exemplo: Se P = 4 , P! = 24 . Logo, a soma de seus algarismos é 2 + 4 = 6.

# Implemente aqui a solução do exercício
# Deus é muito bom, criou a coquinha para nos salvar.
def funcao(p):
    fatorial = 1
    soma = 0
    for i in range(1, p + 1):
        fatorial *= i
    while fatorial:
        soma += fatorial % 10
        fatorial //= 10

    return soma
