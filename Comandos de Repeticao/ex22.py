# Exercício 22: Escreva um programa que leia um número inteiro positivo n e em seguida imprima n linhas do chamado triângulo de Floyd.

# Implemente aqui a solução do exercício
n = int(input())
ultimo = 1
for linha in range(n + 1):
    for _ in range(linha):
        print(f"{ultimo} ", end="")
        ultimo+=1
    print("")
