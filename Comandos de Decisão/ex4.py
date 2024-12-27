# Ler três valores e determinar o maior entre eles.

cont = 3
maior = float('-inf')

while cont > 0:
    a = float(input("Digite um número: "))
    maior = a if maior > a else maior
    cont -= 1

print(f"O maior número é: {maior}")
