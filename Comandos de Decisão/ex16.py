# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor dos números não negativos lidos.

maior = float('-inf')
menor = float('inf')

while True:
    num = int(input())
    if num < 0: break
    if num > maior: maior = num
    if num < menor: menor = num

print(maior, menor)