# Escreva um algoritmo que leia certa quantidade de números inteiros e imprima o maior deles e quantas vezes o maior número foi lido. A quantidade de números a serem lidos deve ser fornecida pelo usuário.

n = int(input())

maior = float("-inf")
cont = 0

for i in range(n):
    a = int(input())
    if a >= maior:
        if a == maior:
            cont += 1
        else:
            maior = a
            cont = 1

print(maior, cont)