# Escreva um programa que leia um número inteiro e calcule a soma de todos os divisores desse número, com exceção dele próprio. Exemplo: a soma dos divisores de 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78.

n = int(input())
soma = 0

for i in range(1, n):
    if n % i == 0:
        soma += i

print(soma)
