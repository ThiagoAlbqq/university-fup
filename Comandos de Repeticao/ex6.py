# Exercício 6: Faça um algoritmo que leia um número N, some todos os números inteiros de 1 a N, e mostre o resultado obtido.

# Implemente aqui a solução do exercício
n = int(input())
sum = 0
for i in range(1, n+1):
    sum += i
print(sum)
