# Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

def soma(a,b): 
    return a + b
def mult(a,b): 
    return a * b
def sub(a,b): 
    return a - b
def div(a,b): 
    return a / b

a = float(input())
escolha = input()
b = float(input())

if escolha == "+": 
    print(f'{soma(a,b):.2f}')
if escolha == "-": 
    print(f'{sub(a,b):.2f}')
if escolha == "*": 
    print(f'{mult(a,b):.2f}')
if escolha == "/": 
    print(f'{div(a,b):.2f}')