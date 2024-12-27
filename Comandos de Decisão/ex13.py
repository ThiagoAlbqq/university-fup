# Calcule as raízes da equação do 2o grau. Lembrando que: x = (−b± √∆)/(2a), onde ∆ = b2 − 4ac, e  ax2 + bx + c = 0 representa uma equação do 2o grau. A variável a tem que ser diferente de zero. Caso seja igual, imprima a mensagem "Nao eh equacao do 2o grau".
# Se ∆ < 0 , não existe raiz real. Imprima a mensagem “Nao existe raiz real”.
# Se ∆ = 0 , existe uma raiz real. Imprima a raiz e a mensagem “Raiz unica”.
# Se ∆ > 0 , Imprima as duas raízes reais.

import math

def raizes(a,b,c):
    delta = b ** 2 - 4*a*c
    if delta < 0: return False, 0, 0
    if delta == 0:
        x = -b/(2*a)
        return True, x, x
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return True, x1, x2

a = float(input())
b = float(input())
c = float(input())

hasRoot, x1, x2 = raizes(a,b,c)
if hasRoot: 
    if x1 == x2:
        print("Raiz unica")
    else:
        print(x1)
        print(x2)
else:
    print("Não existe raiz real")