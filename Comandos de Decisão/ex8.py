# Faça um programa que receba dois números e execute as operações listadas a seguir de acordo com a escolha do usuário:
# 1: Média entre os números digitados
# 2: Diferença do maior pelo menor
# 3: Produto entre os números digitados
# 4: Divisão do primeiro pelo segundo
#Se a opção digitada for inválida, mostrar uma mensagem de erro e terminar a execução doprograma. Dica do Brother: Na operação 4 o segundo número deve ser diferente de 0.

num1 = float(input())
num2 = float(input())
escolha = int(input())

if escolha == 0:
    print("Aqui acabou")

if escolha == 1:
    (num1 + num2) / 2

if escolha == 2:
    if (num1 > num2): 
        num1 - num2
    else: 
        num2 - num1

if escolha == 3:
    num1 * num2

if escolha == 4:
    if (num2 != 0):
        num1/num2