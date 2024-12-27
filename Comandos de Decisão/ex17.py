# Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva, para cada um dos valores lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.

while True: 

    escolha = float(input())
    q = escolha ** 2
    c = escolha ** 3
    sqrt = escolha ** (1/2)

    print(q,c,sqrt)

    if escolha < 0: break