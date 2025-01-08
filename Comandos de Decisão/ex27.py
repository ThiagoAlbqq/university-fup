# Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

maior = 0
menor = 0
cont = int(input())
i = 0

while i < cont:
    a = float(input())
    
    if i == 0:
        maior = a
        menor = a
    
    if a >= maior:
        maior = a
    elif a <= menor:
        menor = a

    i += 1

print(f'{menor:.2f}')
print(f'{maior:.2f}')

