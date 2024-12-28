# Escreva um algoritmo que leia um conjunto de n números e mostre qual foi o menor e o maior valor fornecido.

maior = float("-inf")
menor = float("inf")

array = [1,2,3,4,-1]
cont = 0

while cont < len(array):
    a = array[cont]
    
    if a >= maior:
        maior = a
    elif a <= menor:
        menor = a

    cont += 1

print(menor, maior)
