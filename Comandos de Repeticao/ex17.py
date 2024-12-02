# Exercício 17: Faça um programa que desenhe uma linha na tela usando vários símbolos de igual (Ex: ========). O programa deve ler quantos sinais de iguais serão mostrados.

# Implemente aqui a solução do exercício
n = int(input())
for _ in range(n):
    print("=", end="")
