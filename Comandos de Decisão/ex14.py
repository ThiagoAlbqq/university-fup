# Faça um programa que apresente um menu de opções para o cálculo das seguintes operações entre dois números:
# adição (opção 1)
# subtração (opção 2)
# multiplicação (opção 3)
# divisão (opção 4)
# saída (opção 5)
# O programa deve possibilitar ao usuário a escolha da operação desejada, a exibição do resultado e a volta ao menu de opções. O programa só termina quando for escolhida a opção de saída (opção 5).

def soma(a,b): return a + b
def mult(a,b): return a * b
def sub(a,b): return a - b
def div(a,b): return a / b

while True:
    escolha = int(input())
    if escolha == 5: break
    a = float(input())
    b = float(input())

    if escolha == 1: print(soma(a,b))
    if escolha == 2: print(sub(a,b))
    if escolha == 3: print(mult(a,b))
    if escolha == 4: print(div(a,b))
