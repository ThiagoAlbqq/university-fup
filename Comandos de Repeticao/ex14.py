# Exercício 14: Em Matemática, o número harmônico designado por H(n) define-se como sendo a soma da série harmônica: H(n) = 1/1 + 1/2 + 1/3 ... 1/n. Faça uma função que, dado um valor n inteiro positivo, calcule o valor de H(n).

# Implemente aqui a solução do exercício
# Tenho coragem de procurar ver se está certo - preguiça
def funcao(n):
    harmonicNumber = 0
    for i in range(1,n+1):

        harmonicNumber += 1/i
    return harmonicNumber
