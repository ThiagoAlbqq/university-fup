# Ler três valores e determinar o maior entre eles.

cont = 3
maior = float('-inf')

while cont > 0:
    a = float(input())
    if maior < a: 
        maior = a
    cont -= 1

print(maior)
