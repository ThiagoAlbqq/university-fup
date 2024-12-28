# Faça um algoritmo que leia um número inteiro e imprima seus divisores.

n = int(input())

for i in range(1, n+1):
    if n % i == 0:
        print(i)


