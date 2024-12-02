# Exercício 31: Implemente um programa que leia duas strings, str1 e str2, e um valor inteiro positivo N. Concatene N vezes a string str2 ao final da string str1.

# Implemente aqui a solução do exercício
str1 = input()
str2 = input()
n = int(input())
print(str1, end="")
for i in range(n):
    print(str2, end="")