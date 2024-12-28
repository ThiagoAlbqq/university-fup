# Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua média.

soma = 0
contador = 0

while contador <= 10:
    num = int(input())
    if num >=0:
        soma += num
        contador += 1

print(soma/contador)