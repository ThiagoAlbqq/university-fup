# Exercício 3: Faça um programa que peça ao usuário para digitar 10 valores e mostre a soma deles.

# Implemente aqui a solução do exercício
sum = 0
for i in range(0,10):
    x = float(input())
    sum += x
print(f"{sum:.2f}")
