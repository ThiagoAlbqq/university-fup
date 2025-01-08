# Exercício 19: Crie uma função que receba como parâmetro um valor inteiro e gere como saída n linhas como pontos de exclamação, conforme o exemplo abaixo (para n = 5).

# Implemente aqui a solução do exercício
def imprima_n_vezes(x, n):
    for _ in range(n):
        print(x, end=" ")
    print()

def funcao(n):
    for i in range(1,n+1):
        imprima_n_vezes("!", i)
