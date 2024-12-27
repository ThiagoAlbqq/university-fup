# Faça um programa que receba dois numeros inteiros e imprima o maior deles, se por acaso os dois numeros forem iguai, imprima a mensagem  "Numeros iguais"

a = input()
b = input()

if a == b:
    print("Números iguais")
else:
    if a > b:
        print(a)
    else: 
        print(b)
