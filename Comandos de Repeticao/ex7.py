# Exercício 7: Faça uma função que, dado número N, some todos os números inteiros de 1 a N, e retorne o resultado obtido.

# Implemente aqui a solução do exercício
def funcao(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum
print(funcao(9))
