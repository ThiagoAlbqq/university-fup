# Elabore um programa que faça leitura de vários números inteiros, até que se digite um número negativo. O programa tem que retornar o maior e o menor dos números não negativos lidos.

maior = -1
menor = -1
contador = 0

while True:
    num = int(input())
    if num < 0: break
    if contador == 0:
        maior = num
        menor = num
    if num > maior: maior = num
    if num < menor: menor = num
    
    contador += 1

if maior != -1:
    print(maior)
    print(menor)