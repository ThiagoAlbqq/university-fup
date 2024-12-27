# Faça um programa que simule uma calculadora com as 4 operações básicas. O usuário digita o primeiro número, escolhe a operação e em seguida digita o segundo número, exatamente nessa ordem. O programa deve mostrar o resultado da operação.

def soma(a,b): return a + b
def mult(a,b): return a * b
def sub(a,b): return a - b
def div(a,b): return a / b

escolha = int(input())
a = float(input())
b = float(input())

if escolha == 1: soma(a,b)
if escolha == 2: sub(a,b)
if escolha == 3: mult(a,b)
if escolha == 4: div(a,b)