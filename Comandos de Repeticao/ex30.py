# Exercício 30: Faça um programa que receba uma palavra e a imprima de trás-para-frente.

# Implemente aqui a solução do exercício
word = input()
for i in range(len(word)-1, -1, -1):
    print(word[i])
