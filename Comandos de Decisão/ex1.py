# Faça um programa que receba dois numeros inteiros e imprima o maior deles, se por acaso os dois numeros forem iguai, imprima a mensagem  "Numeros iguais"

a = int(input())
b = int(input())

if a == b:
    print("Numeros iguais")
else:
    if a > b:
        print(a)
    else: 
        print(b)
