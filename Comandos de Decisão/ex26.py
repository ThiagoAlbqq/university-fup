# Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor lido.

maior = float("-inf")
menor = float("inf")

cont = 10

while cont > 0:
    a = int(input("Digite um número: "))
    
    if a >= maior:
        maior = a
    elif a <= menor:
        menor = a

    cont -= 1

print(menor, maior)
