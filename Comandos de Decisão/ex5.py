# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadradado número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido. 
import math
a = float(input())

if a > 0: 
    print(f'{math.sqrt(a):.2f}')
else:
    print("Numero invalido")