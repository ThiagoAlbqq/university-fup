# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

maior = 0
menor = 0

cont = 0

while cont < 10:
    a = int(input())
    
    if cont == 0:
        maior = a
        menor = a
    
    if a >= maior:
        maior = a
    elif a <= menor:
        menor = a

    cont += 1

print(f'{menor:.2f}')
print(f'{maior:.2f}')
