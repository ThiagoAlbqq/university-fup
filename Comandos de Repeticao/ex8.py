# Exercício 8: Faça um programa que leia um número inteiro N e depois imprima os N primeiros números naturais ímpares.

# Implemente aqui a solução do exercício
n = int(input())
for i in range(0, n+1):
    if i % 2 != 0:
        print(i)
