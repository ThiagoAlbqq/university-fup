# Exercício 4: Faça um programa que leia 10 inteiros e imprima sua média.

# Implemente aqui a solução do exercício
sum = 0
for i in range(0,10):
    x = int(input())
    sum += x
media = sum/10
print(media)
