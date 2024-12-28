# Elabore uma função que receba três notas de um aluno como parâmetros e uma letra. Se a letra for A, a função deverá calcular a média aritmética das notas do aluno; se for P, deverá calcular a média ponderada, com os pesos 5, 3, 2.

n1 = float(input())
n2 = float(input())
n3 = float(input())
letra = input()

def funcao(n1, n2, n3, letra):
    if letra == "A":
        return (n1 + n2 + n3)/ 3
    elif letra == "P":
        return ( n1 * 5 + n2 * 3 + n3 * 2)/ 10
    
    
    