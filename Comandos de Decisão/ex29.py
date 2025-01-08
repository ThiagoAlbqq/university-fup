# Faça um programa que receba um valor inteiro n ≥ 0 e imprima se esse número é primo ou não.

n = int(input())

def funcao(n):
    if n == 1:
        return "Nao primo"
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return "Nao primo"
    return "Primo"

print(funcao(n))