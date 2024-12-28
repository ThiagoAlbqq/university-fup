# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

n = int(input())

def funcao(n):
    for i in range(1, n):
        if i == 1 or n:
            continue
        
        if n % i == 0:
            return False
    return True

print(funcao(n))
